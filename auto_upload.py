#! /usr/bin/python3
import config, helpers, os, re

if __name__ == "__main__":
	path = config.usenet_dir
	configfile = '/home/***REMOVED***/.gopoststuff.mv.conf'
	pathname = re.findall(r"\/(\w+)", path)[-1]
	logger = helpers.setup_logger(pathname)
	helpers.is_running(path, logger)
	items = os.listdir(path)
	for item in items:
		if helpers.is_directory(path, item):
			continue
		filename = helpers.find_tv_show(item, logger)
		if not filename:
			continue
		filename = helpers.cleanup_name(filename)
		filename = helpers.translate_format(filename)
		helpers.upload(item, filename, path, logger)

	os.remove(path + 'running')

