# Importing re module
import re

# Initializing text and pattern
pattern=["Life","Journey"]
s1="Life is a Journey not a destination. life Life is a journey with a problems to solve."
# Iterating over the text to search for pattern
for i in pattern:
    print("Searching in s1 ",i)
    print(re.findall(i,s1, re.IGNORECASE))
        	
