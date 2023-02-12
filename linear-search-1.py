# Search function with parameter list name
# and the value to be searched


def search(List, n):

	for i in range(len(List)):
		if List[i] == n:
			return True
	return False


# list which contains both string and numbers.
List = [1, 2, 3, 4, 5, 6]

# Driver Code
n = 4

if search(List, n):
	print("position value of")
else:
	print("Not Found")
