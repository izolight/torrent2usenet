#! /usr/bin/python3
import shutil, os, re, config, sys, logging, helpers

FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
RUNNING = 'manual.running'

logging.basicConfig(format=FORMAT,filename='/var/log/t2u/manual.log',level=logging.DEBUG)
logger = logging.getLogger('torrent2usenet')

if (os.path.isfile(config.manual_dir + RUNNING)):
	logger.warning('Script already running, exiting.')
	sys.exit()

os.system('touch ' + config.manual_dir + RUNNING)

directory = os.listdir(config.manual_dir)

for filename in directory:
	if filename == RUNNING:
		continue
	if helpers.is_directory(config.manual_dir, filename):
		continue

	logger.info('Processing %s' % filename)

	new_filename = re.sub(r"\,","",filename)
	new_filename = re.sub(r"\(|\)",".",new_filename)
	new_filename = re.sub(r" - ","-",new_filename)
	new_filename = re.sub(r"\s",".",new_filename)
	new_filename = re.sub(r"\'","",new_filename)
	new_filename = re.sub(r"\`","",new_filename)
	new_filename = re.sub(r"드라마\.*\s*스페셜", "Drama.Special", new_filename)
	logger.info('Clean name is %s' % new_filename)

	foldername = re.sub(r"\.(MP4|mp4|ts|tp|mkv|avi)$","",new_filename)
	os.mkdir(config.manual_dir + foldername) # make folder without file ending			
	shutil.move(config.manual_dir + filename, config.manual_dir + foldername + "/" + new_filename) # move file to folder
	
	logger.info('Starting rarnpar on %s' % foldername)
	os.system("rarnpar -D " + config.manual_dir + foldername) # rar n par	
	os.remove(config.manual_dir + foldername + "/" + new_filename) # remove video
	logger.info('Starting GoPostStuff on %s' % foldername)
	os.system('GoPostStuff -d ' + config.manual_dir + foldername) # post rar n pars
#	os.system('GoPostStuff-newsoo -c="/home/***REMOVED***/.newsoo.gopoststuff.conf" -d ' + config.manual_dir + foldername) # post rar n pars
	logger.info('Posted to Usenet, deleting remaining files.')
	shutil.rmtree(config.manual_dir + foldername) # remove files						

os.remove(config.manual_dir + RUNNING)
