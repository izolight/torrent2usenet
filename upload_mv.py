#! /usr/bin/python3
import shutil,os,re,config,sys

RUNNING = 'm2u.running'

def clean_names(name):
	new_filename = re.sub(r"\,","",name)
	new_filename = re.sub(r"\!","",new_filename)
	new_filename = re.sub(r"\s*\(",".",new_filename)
	new_filename = re.sub(r"\)\s*",".",new_filename)
	new_filename = re.sub(r" - ",".",new_filename)
	new_filename = re.sub(r"\&","+",new_filename)
	new_filename = re.sub(r"\'","",new_filename)
	new_filename = re.sub(r"\s",".",new_filename)

	foldername = re.sub(r"\.[MP4|mp4|ts|tp|mkv|avi]$","",new_filename)

	return new_filename, foldername

def upload(file_name, new_name, folder_name):
	os.mkdir(config.music_dir + folder_name)
	shutil.move(config.music_dir + file_name, config.music_dir + folder_name + "/" + new_name)
	os.system("rarnpar -N -D " + config.music_dir + folder_name)
	os.remove(config.music_dir + folder_name + "/" + new_name)
	os.system('GoPostStuff -c="/home/***REMOVED***/.gopoststuff.mv.conf" -d '+ config.music_dir + folder_name)
	shutil.rmtree(config.music_dir + folder_name)	

if (os.path.isfile(config.music_dir + RUNNING)):
        print('script already running, exiting')
        sys.exit()

os.system('touch ' + config.music_dir + RUNNING)

directory = os.listdir(config.music_dir)

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

os.remove(config.music_dir + RUNNING)
