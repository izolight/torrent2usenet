#! /usr/bin/python3
import shutil,os

directory = os.listdir()

for filename in directory:
	foldername = filename[:-4]
	os.mkdir(foldername) # make folder without file ending			
	shutil.move(filename, foldername) # move file to folder
	os.system("rarnpar -N -D " + foldername) # rar n par
	os.remove(foldername + "/" + filename) # remove video
	os.system("GoPostStuff -d " + foldername) # post rar n pars
	shutil.rmtree(foldername) # remove files						
