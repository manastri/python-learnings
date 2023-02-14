import os,re

def write_data(source, destination):
    if not os.path.isdir(destination):
        os.mkdir(destination, 777)

    for file in os.listdir(source):
        if re.search("\.txt$", file):
            with open(source+'/'+file,'r') as f, open(destination+'/'+file,'a') as s:
                for line in f:
                    s.write(line)

write_data('/Users/mtripathy/Documents/python-learnings','FolderC')
write_data('/Users/mtripathy/Documents/python-learnings/FolderB','FolderC')