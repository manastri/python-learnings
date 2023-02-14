def Palindrome(text):
    if len(text) == 1:
        return text + " is a Palindrome"
    else:
        if text == text[::-1]:
            return text + " is a Palindrome"
        else:
            return text + " is NOT a Palindrome"

print(Palindrome("RADAR"))