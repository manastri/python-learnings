# Importing re module
import re

# Initializing text and pattern
pattern=["Life","Journey"]
s1="Life is a Journey not a destination"

# Iterating over the text to search for pattern
for i in pattern:
    print("Searching ",i)
    if(re.match(i,s1)):
        print("Match found at the beginning ---",i, "in found in the string - ", s1)
    else:
        print("Match not found at the beginning ---",i," not found in the string - ", s1)  
