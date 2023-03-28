def doubler(n):
    return lambda a: a * n
mydoubler = doubler(2)

print(mydoubler(10))