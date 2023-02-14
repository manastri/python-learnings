fin = open("/Users/mtripathy/Documents/python-learnings/file-with-multiple-space.txt", "rt")
fout = open("/Users/mtripathy/Documents/python-learnings/out.txt", "wt")

for line in fin:
 print(line)
 fout.write(' '.join(line.split()))
	
fin.close()
fout.close()