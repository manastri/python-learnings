def sum(n):
    if n < 10:
        return n
    else:
        allDigits = n // 10
        lastDigit = n % 10
        return sum(allDigits) + lastDigit

print("Sum of digits :" , sum(2222))

