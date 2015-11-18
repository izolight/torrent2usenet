#! /usr/bin/python3
import re, logging, os, sys, shutil
from multiprocessing import Process
import config
from dict import names

class Uploader:
    def __init__(self, configuration):
        self.path = configuration['dir']
        self.prefix = configuration['prefix']
        self.fromname = configuration['from']
        self.group = configuration['group']
        self.server = configuration['server']
        self.host = configuration['host']        
        self.name = re.findall(r"\/(\w+)", self.path)[-1]
        self.items = os.listdir(self.path)

    FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
    RUNNING = 'running'

    def setup_logger(self):
        logging.basicConfig(format=self.FORMAT, filename='/var/log/t2u/'+self.name+'.log', level = logging.DEBUG)
        self.logger = logging.getLogger('torrent2usenet')

    def is_running(self):
        if (os.path.isfile(self.path + self.RUNNING)):
            self.logger.warning('Script already running, exiting.')
            sys.exit()
        else:
            os.system('touch ' + self.path + self.RUNNING)

    def is_directory(self, filename):
        if (os.path.isdir(os.path.join(self.path, filename))):
            return True
        if filename == self.RUNNING:
            return True
        return False

    def find_tv_show(self, filename):
        for key in names:
            if (re.search(names[key],filename)):
                self.logger.info('Matched %s to %s' % (filename, key))
                english_name = re.sub(names[key],key,filename)
                return english_name
        return False

    def cleanup_name(self,filename):
        # Remove Tags ex [MBC]
        filename = re.sub(r"\[.+?\]\s?", "", filename)
        # Remove unwanted characters
        filename = re.sub(r"「|」|\,|\'|\´|\`|\!", "", filename)
        filename = re.sub(r" - ", "-", filename)
        filename = re.sub(r"\&", "+", filename)
        # Replace unwanted charaters with dots
        filename = re.sub(r"\,|\(|\)|\s+", ".", filename)
        # Replace all multiple occurences of dots with just one
        filename = re.sub(r"\.+", ".", filename)
        filename = re.sub(r"\.-\.", "-", filename)
        return filename

    def translate_format(self, filename):
        # Episode Numbers
        filename = re.sub(r"(\d{1,2})부", r"E\1", filename)
        filename = re.sub(r"(?:제)*(\d{1,3})(?:화|회)", r"E\1", filename)
        filename = re.sub(r"_0+(\d+)_2M", r".E\1", filename)
        # Season Numbers
        filename = re.sub(r"시즌","S", filename)
        # Special Meanings
        filename = re.sub(r"플러스", "Plus", filename)
        filename = re.sub(r"페스티벌", "Festival", filename)
        filename = re.sub(r"추석특집", "Chuseok.Special", filename)
        filename = re.sub(r"신년특집", "New.Year.Special", filename)
        filename = re.sub(r"설날특집", "Lunar.New.Year.Special", filename)
        filename = re.sub(r"설 특집", "Lunar.New.Year.Special", filename)
        filename = re.sub(r"설특선", "Lunar.New.Year.Special", filename)
        filename = re.sub(r"드라마\.*\s*스페셜", "Drama.Special", filename)
        filename = re.sub(r"다큐멘터리", "Documentary", filename)
        filename = re.sub(r"감독편집판", "Directors.Cut", filename)
        filename = re.sub(r"TV\.*문\.*학\.*관", "TV.Feature", filename)
        filename = re.sub(r"현장 스토리", "Behind.the.Scenes", filename)
        return filename
        
    def generate_foldername(self, filename, tv):
        foldername = re.sub(r"\.(MP4|mp4|ts|tp|mkv|avi|wmv|m2t)$", "", filename)
        if tv:
            foldername = re.sub(r"[^\w]{2,}", ".", foldername)
        return foldername
    
    def move_files(self, originalname, foldername):
        os.mkdir(self.path + foldername)
        cleanedname = self.cleanup_name(originalname)
        shutil.move(self.path + originalname, self.path + foldername + "/" + cleanedname)
        return cleanedname

    def rarnpar(self, foldername):
        self.logger.info('Starting rarnpar on %s' % foldername)
        os.system('rarnpar -n -D ' + self.path + foldername)

    def upload(self, foldername):
        self.logger.info('Starting GoPostStuff on %s' % foldername)
        gopoststuff = 'gopoststuff -c %s -prefix %s -from "%s" -g %s -server %s -host %s -nzb %s -d %s' %(config.config_file, self.prefix, self.fromname, self.group, self.server, self.host, config.nzb_path + foldername + '.nzb', self.path + foldername)
        os.system(gopoststuff)
        self.logger.info('Upload finished, deleting remaining files.')
        shutil.rmtree(self.path + foldername)

    def process(self, tv=False, mv=False):
        self.setup_logger()
        self.is_running()
        for item in self.items:
            if self.is_directory(item):
                if mv:
                    for f in os.listdir(os.path.join(self.path, item)):
                        if "Cap" in f:
                            shutil.rmtree(self.path + item + "/" + f)
                        else:
                            shutil.move(self.path + item + "/" + f, self.path + f)
                    shutil.rmtree(self.path + item)
                    continue
                else:
                    continue
            if tv:
                filename = self.find_tv_show(item)
            else:
                filename = item
            if not filename:
                continue
            filename = self.cleanup_name(filename)
            filename = self.translate_format(filename)
            foldername = self.generate_foldername(filename, tv)
            cleanedname = self.move_files(item, foldername)
            self.rarnpar(foldername)
            os.remove(self.path + foldername + "/" + cleanedname)
            self.upload(foldername)
        os.remove(self.path + self.RUNNING)

if __name__ == "__main__":
    tv_uploader = Uploader(config.tv)
    p1 = Process(target=tv_uploader.process, kwargs={'tv':True})
    movie_uploader = Uploader(config.movie)
    p2 = Process(target=movie_uploader.process)
    music_uploader = Uploader(config.music)
    p3 = Process(target=music_uploader.process, kwargs={'mv':True})
    manual_uploader = Uploader(config.manual)
    p4 = Process(target=manual_uploader.process)
    jap_uploader = Uploader(config.jap)
    p5 = Process(target=jap_uploader.process)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
