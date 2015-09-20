#! /usr/bin/python3
import config, helpers, os, re, shutil

def upload(originalname, filename, path, logger, configfile):
	foldername = helpers.create_foldername(filename)
	os.mkdir(path + foldername)
	shutil.move(path + originalname, path + foldername + "/" + originalname)
	logger.info('Starting rarnpar on %s' % foldername)
	os.system('rarnpar -N -D ' + path + foldername)
	os.remove(path + foldername + "/" + originalname)
	logger.info('Starting GoPostStuff on %s' % foldername)
	os.system('GoPostStuff-newsoo -c="' + configfile + '" -d ' + path + foldername)
	logger.info('Upload finished, deleting remaining files.')
	shutil.rmtree(path + foldername)

if __name__ == "__main__":
	path = config.movie_dir
	configfile = '/home/***REMOVED***/.newsoo.movie.gopoststuff.conf'
	pathname = re.findall(r"\/(\w+)", path)[-1]
	logger = helpers.setup_logger(pathname)
	helpers.is_running(path, logger)
	items = os.listdir(path)
	for item in items:
		if helpers.is_directory(path, item):
			continue
		#filename = helpers.find_tv_show(item, logger)
		#if not filename:
		#	continue
		filename = helpers.cleanup_name(item)
		filename = helpers.translate_format(filename)
		upload(item, filename, path, logger, configfile)

	os.remove(path + 'running')
