#! /usr/bin/python3
import re, shutil, os, sys, logging
from dict import names

RUNNING = 'running'
FORMAT = '%(asctime)s %(levelname)-8s %(message)s'

def setup_logger(dir_name):
	logging.basicConfig(format=FORMAT, filename='/var/log/t2u/'+dir_name, level=logging.DEBUG)
	logger = logging.getLogger('torrent2usenet')
	return logger

def is_running(path, logger):
	if (os.path.isfile(path + RUNNING)):
		logger.warning('Script already running, exiting.')
		sys.exit()
	else:
		os.system('touch ' + path + RUNNING)	

def find_tv_show(filename, logger):
	for key in names:
		if (re.search(names[key],filename)):
			logger.info('Matched %s to %s' % (filename, key))
			english_name = re.sub(names[key],key,filename)
			return english_name
	return False

def is_directory(path, filename):
	if (os.path.isdir(os.path.join(path, filename))):
		return True
	if filename == 'running':
		return True
	else:
		return False

def cleanup_name(filename):
	# Remove Tags ex [MBC]
	filename = re.sub(r"\[[^\[\]]+\]\s?", "", filename)
	# Remove unwanted characters
	filename = re.sub(r"「|」|\,|\'|\´|\`|\!", "", filename)
	filename = re.sub(r" - ", "-", filename)
	filename = re.sub(r"\&", "+", filename)
	# Replace unwanted charaters with dots
	filename = re.sub(r"\,|\(|\)|\s+", ".", filename)
	return filename

def translate_format(filename):
	# Episode Numbers
	filename = re.sub(r"(\d{1,2})부", r"E\1", filename)
	filename = re.sub(r"(?:제)*(\d{1,3})(?:화|회)", r"E\1", filename)
	# Season Numbers
	filename = re.sub(r"시즌","S", filename)
	# Special Meanings
	filename = re.sub(r"페스티벌", "Festival", filename)
	filename = re.sub(r"신년특집", "New.Year.Special", filename)
	filename = re.sub(r"설날특집", "Lunar.New.Year.Special", filename)
	filename = re.sub(r"설 특집", "Lunar.New.Year.Special", filename)
	filename = re.sub(r"설특선", "Lunar.New.Year.Special", filename)
	filename = re.sub(r"드라마\.*\s*스페셜", "Drama.Special", filename)
	filename = re.sub(r"다큐멘터리", "Documentary", filename)
	filename = re.sub(r"감독편집판", "Directors.Cut", filename)
	filename = re.sub(r"TV\.*문\.*학\.*관", "TV.Feature", filename)
	return filename

def create_foldername(filename):
	foldername = re.sub(r"\.(MP4|mp4|ts|tp|mkv|avi|wmv)$", "", filename)
	return foldername

def upload(originalname, filename, path, logger):
	foldername = create_foldername(filename)
	os.mkdir(path + foldername)
	cleanedname = cleanup_name(originalname)
	shutil.move(path + originalname, path + foldername + "/" + cleanedname)
	logger.info('Starting rarnpar on %s' % foldername)
	os.system('rarnpar -D ' + path + foldername)
	os.remove(path + foldername + "/" + cleanedname)
	logger.info('Starting GoPostStuff on %s' % foldername)
	os.system('GoPostStuff -d ' + path + foldername)
	logger.info('Upload finished, deleting remaining files.')
	shutil.rmtree(path + foldername)
