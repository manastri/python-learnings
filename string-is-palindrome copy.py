#Function to define palindrom
def palindrome(text):
    if len(text) == 1:
        return text + " is a palindrome"
    else:
        if text == text [::-1]:
            return text + " is a palindrome"
        else:
            return text + " is not a palindrome"
print(palindrome("MANAS"))
    
