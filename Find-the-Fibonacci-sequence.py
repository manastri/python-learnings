def fib(n):
    if n <= 1:
        return n
    return (fib(n-1) + fib(n-2))

term = 10
print("Fibonacci sequence : ")
for i in range(term):
    print(fib(i))