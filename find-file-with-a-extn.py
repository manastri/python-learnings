# import library
import re,os

#Source location
source = '/Users/mtripathy/Documents/python-learnings/'

#list out the files in a directory

files = os.listdir(source)

for file in files:
	# search given pattern in the line
	match = re.search("\.txt$", file)
	# if match is found
	if match:
		print("The file ending with .txt is:",
			file)
