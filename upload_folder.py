#! /usr/bin/python3
import shutil,os,re

directory = os.listdir()

for filename in directory:
	new_filename = re.sub(r"\,","",filename)
	new_filename = re.sub(r"\(|\)",".",new_filename)
	new_filename = re.sub(r" - ","-",new_filename)
	new_filename = re.sub(r"\s",".",new_filename)
	new_filename = re.sub(r"\'","",new_filename)
	new_filename = re.sub(r"드라마\.*\s*스페셜", "Drama.Special", new_filename)
	foldername = re.sub(r"\.\w*$","",new_filename)
	os.mkdir(foldername) # make folder without file ending			
	shutil.move(filename, foldername + "/" + new_filename) # move file to folder
	os.system("rarnpar -b 2304000 -N -D " + foldername) # rar n par
	os.remove(foldername + "/" + new_filename) # remove video
	os.system("GoPostStuff -d " + foldername) # post rar n pars
	shutil.rmtree(foldername) # remove files						
