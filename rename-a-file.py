import os

old_file_name = "/Users/mtripathy/Documents/python-learnings/testfile"
new_file_name = "/Users/mtripathy/Documents/python-learnings/testfile-renamed"

try :
	os.rename(old_file_name, new_file_name)
	print('File renamed successfully.')
except:
	print('Could not rename file.')
	print('An exception occurred.')