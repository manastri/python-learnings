
text = "MANAS"
print("Using String slicing : " + text[::-1])

newText = ''
for i in text:
    newText = i + newText
print("Using for loop : " + newText)