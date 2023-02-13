#Count how many times a word occurred in given Text File
#get file object reference to the file
file = open("/Users/mtripathy/Documents/python-learnings/LICENSE", "r")

#read content of file to string
data = file.read()

#get number of occurrences of the substring in the string
occurrences = data.count("GNU")

print('Number of occurrences of the word :', occurrences)