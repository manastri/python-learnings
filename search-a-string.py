# Importing re module
import re

# Initializing text and pattern
pattern=["Life","journey"]
s1="Life is a Journey not a destination"

# Iterating over the text to search for pattern
for i in pattern:
    print("Searching ",i)
    if(re.search(i,s1)):
        print("Found ",i, "in the string - ", s1)
    else:
        print(i," not found in the string - ", s1)   
