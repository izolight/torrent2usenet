#! /usr/bin/python3
import shutil, os, re, config, sys, logging

FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
RUNNING = 'm2u.running'

logging.basicConfig(format=FORMAT,filename='/var/log/t2u/music.log',level=logging.DEBUG)
logger = logging.getLogger('torrent2usenet')

def clean_names(name):
	logger.info('Processing %s' % name)
	new_filename = re.sub(r"\,","",name)
	new_filename = re.sub(r"\!","",new_filename)
	new_filename = re.sub(r"\s*\(",".",new_filename)
	new_filename = re.sub(r"\)\s*",".",new_filename)
	new_filename = re.sub(r" - ",".",new_filename)
	new_filename = re.sub(r"\&","+",new_filename)
	new_filename = re.sub(r"\'","",new_filename)
	new_filename = re.sub(r"\s",".",new_filename)
	logger.info('Clean name is %s' % new_filename)	

	foldername = re.sub(r"\.(MP4|mp4|ts|tp|mkv|avi)$","",new_filename)
	return new_filename, foldername

def upload(file_name, new_name, folder_name):
	os.mkdir(config.music_dir + folder_name)
	shutil.move(config.music_dir + file_name, config.music_dir + folder_name + "/" + new_name)
	logger.info('Starting rarnpar on %s' % folder_name)
	os.system("rarnpar -N -D " + config.music_dir + folder_name)
	os.remove(config.music_dir + folder_name + "/" + new_name)
	logger.info('Starting GoPostStuff on %s' % folder_name)
	os.system('GoPostStuff -c="/home/***REMOVED***/.gopoststuff.mv.conf" -d '+ config.music_dir + folder_name)
	logger.info('Upload finished, deleting remaining files.')
	shutil.rmtree(config.music_dir + folder_name)	

if (os.path.isfile(config.music_dir + RUNNING)):
	logger.warning('Script already running, exiting')
	sys.exit()

os.system('touch ' + config.music_dir + RUNNING)

directory = os.listdir(config.music_dir)
#logger.info('Start uploading Musicvideos.')

for filename in directory:
	if (os.path.isdir(os.path.join(config.music_dir, filename))):
		for f in os.listdir(os.path.join(config.music_dir, filename)):
			if "Cap" in f:
				shutil.rmtree(config.music_dir + filename + "/" + f)
			else:
				new_filename, foldername = clean_names(f)
				upload(filename + "/" + f,new_filename,foldername)
		shutil.rmtree(config.music_dir + filename)
	elif "m2u.running" in filename:
		continue
	else:
		new_filename, foldername = clean_names(filename)
		upload(filename,new_filename,foldername)

#logger.info('Finished Music Upload.')
os.remove(config.music_dir + RUNNING)
