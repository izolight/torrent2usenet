#! /usr/bin/python3
import re, shutil, os, sys, config
from dict import names

RUNNING = 't2u.running'

if (os.path.isfile(config.usenet_dir + RUNNING)):
	print('script already running, exiting')
	sys.exit()

os.system('touch ' + config.usenet_dir + RUNNING)

directory = os.listdir(config.usenet_dir)

for filename in directory:
	if (os.path.isdir(os.path.join(config.usenet_dir, filename))):
		if "HDione" in filename:
			shutil.move(config.usenet_dir + filename + "/" + filename + ".mkv", config.usenet_dir + filename + ".mkv")
			shutil.rmtree(config.usenet_dir + filename)
		continue
	else:
		for key in names:
			if (re.search(names[key],filename)):
				print(key)
				# convert to english
				new_filename = re.sub(names[key],key,filename)
				new_filename = re.sub(r"\,",".",new_filename)
				new_filename = re.sub(r"\(|\)",".",new_filename)
				new_filename = re.sub(r"\[.*\]\s*","",new_filename)
				new_filename = re.sub(r"\.내정보","",new_filename)
				new_filename = re.sub(r"\s",".",new_filename)
				new_filename = re.sub(r"(\d{1,2})부", r"E\1", new_filename)
				new_filename = re.sub(r"(?:제)*(\d{1,3})(?:화|회)", r"E\1", new_filename)
				new_filename = re.sub(r"0{3}?(\d{2})\_2M", r"E\1", new_filename)
				new_filename = re.sub(r"시즌","S", new_filename)
				new_filename = re.sub(r"신년특집", "New.Year.Special", new_filename)
				new_filename = re.sub(r"설날특집", "Lunar.New.Year.Special", new_filename)
				new_filename = re.sub(r"설 특집", "Lunar.New.Year.Special", new_filename)
				new_filename = re.sub(r"설특선", "Lunar.New.Year.Special", new_filename)	
				new_filename = re.sub(r"드라마\.*\s*스페셜", "Drama.Special", new_filename)
				new_filename = re.sub(r"다큐멘터리", "Documentary", new_filename)
				new_filename = re.sub(r"감독편집판", "Directors.Cut", new_filename)
	#			new_filename = re.sub(r"스페셜", "Special", new_filename)
				new_filename = re.sub(r"TV\.*문\.*학\.*관", "TV.Feature", new_filename)
				cleanname = re.sub(r"\,",".",filename)
				cleanname = re.sub(r"\(|\)",".",cleanname)
				os.rename(config.usenet_dir + filename, config.usenet_dir + cleanname)
#				foldername = re.sub(r"\.\w*$","",new_filename)
				os.mkdir(config.usenet_dir + new_filename) # make folder			
				shutil.move(config.usenet_dir + cleanname, config.usenet_dir + new_filename) # move file to folder
				os.system("rarnpar -b 2304000 -D " + config.usenet_dir + new_filename) # rar n par
				os.remove(config.usenet_dir + new_filename + "/" + cleanname) # remove video
				os.system("GoPostStuff -d "+ config.usenet_dir + new_filename) # post rar n pars
				shutil.rmtree(config.usenet_dir + new_filename) # remove files						

os.remove(config.usenet_dir + RUNNING)
sys.exit()
