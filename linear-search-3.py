# Search function with parameter tuple name
# and the value to be searched


def search(Tuple, n):

	for i in range(len(Tuple)):
		if Tuple[i] == n:
			return True
	return False


# Tuple which contains both string and numbers.
Tuple = (1, 2, 'sachin', 4, 'ramesh', 6)


# Driver Code
n = 'ramesh'

if search(Tuple, n):
	print("Found")
else:
	print("Not Found")
