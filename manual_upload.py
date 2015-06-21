#! /usr/bin/python3
import shutil,os,re,config,sys

RUNNING = 'manual.running'

if (os.path.isfile(config.manual_dir + RUNNING)):
        print('script already running, exiting')
        sys.exit()

os.system('touch ' + config.manual_dir + RUNNING)

directory = os.listdir(config.manual_dir)
if directory == []:
	sys.exit()

for filename in directory:
	new_filename = re.sub(r"\,","",filename)
	new_filename = re.sub(r"\(|\)",".",new_filename)
	new_filename = re.sub(r" - ","-",new_filename)
	new_filename = re.sub(r"\s",".",new_filename)
	new_filename = re.sub(r"\'","",new_filename)
	new_filename = re.sub(r"\`","",new_filename)
	new_filename = re.sub(r"드라마\.*\s*스페셜", "Drama.Special", new_filename)
	foldername = re.sub(r"\.\w*$","",new_filename)
	os.mkdir(config.manual_dir + foldername) # make folder without file ending			
	shutil.move(config.manual_dir + filename, config.manual_dir + foldername + "/" + new_filename) # move file to folder
	os.system("rarnpar -b 2304000 -N -D " + config.manual_dir + foldername) # rar n par
	os.remove(config.manual_dir + foldername + "/" + new_filename) # remove video
	os.system("GoPostStuff -d " + config.manual_dir + foldername) # post rar n pars
	shutil.rmtree(config.manual_dir + foldername) # remove files						

os.remove(config.manual_dir + RUNNING)

