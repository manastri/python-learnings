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
n = int(input("Enter your Number : "))

if search(List, n):
	print("Found")
else:
	print("Not Found")
