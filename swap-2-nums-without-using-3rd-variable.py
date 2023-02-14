a, b = 10, 20
a, b = b, a
print("Using in-build syntax : a is" , a , "& b is" , b)

a, b = 10, 20
a = a + b
b = a - b
a = a - b
print("Using arithmetic operations : a is" , a , "& b is" , b)