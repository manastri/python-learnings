import os

path ="/Users/mtripathy/Documents/python-learnings"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		if(file.endswith(".py")):
			print(os.path.join(root,file))
