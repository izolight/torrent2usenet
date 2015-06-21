#! /usr/bin/python3
import shutil,os,re,config,sys

RUNNING = 'm2u.running'

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
				shutil.move(config.music_dir + filename + "/" + f, config.music_dir + f)
		shutil.rmtree(config.music_dir + filename)
	if "m2u.running" in filename:
		continue
	else:
		new_filename = re.sub(r"\,","",filename)
		new_filename = re.sub(r"\!","",new_filename)
		new_filename = re.sub(r"\s*\(",".",new_filename)
		new_filename = re.sub(r"\)\s*",".",new_filename)
		new_filename = re.sub(r" - ",".",new_filename)
		new_filename = re.sub(r"\&","+",new_filename)
	#	new_filename = re.sub(r"\] ","\]",new_filename)
		new_filename = re.sub(r"\'","",new_filename)
		new_filename = re.sub(r"\s",".",new_filename)
		foldername = re.sub(r"\.\w*$","",new_filename)
		os.mkdir(config.music_dir + foldername) # make folder without file ending			
		shutil.move(config.music_dir + filename, config.music_dir + foldername + "/" + new_filename) # move file to folder
		os.system("rarnpar -N -D " + config.music_dir + foldername) # rar n par
		os.remove(config.music_dir + foldername + "/" + new_filename) # remove video
		os.system('GoPostStuff -c="/home/***REMOVED***/.gopoststuff.mv.conf" -d '+ config.music_dir + foldername) # post rar n pars
		shutil.rmtree(config.music_dir + foldername) # remove files						

os.remove(config.music_dir + RUNNING)
