def locate_card(cards, query):
    #create a variable position with the value 0
    position = 0
    hi = len(cards) - 1
    print("the high value is :", hi)

    # Set up a loop for repitition
    while position <= hi :

#Check if the element at the current position matches the query
        print("the high value is in while loop :", hi)
        print("the position value is in while loop:", position)
        if cards[position] == query:
            print("the position value is in first if:", position)
        #Answer found return and exit..
            return True
#increment the position
        position += 1
        print("the position value after increase:", position)
        #Check if we have reached the end of the array

        if position == len(cards):
            print("we reach max")

#Number not found, return 2
            return False

cards = [4, 6, 8, 9, 12, 14, 16, 18]
query = int(input("Enter your query: "))
#query = 18

if locate_card(cards, query):
	print("Found ")
else:
	print("Not Found")
