def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * factorial(n-1)

num = 4
print(factorial(num))


# Fibonacci series
def fib(n):
    a = 0
    b = 1
    if n==1:
        return a
    else:
        print(a)
        print(b)
    
    for i in range(2,n):
        c=a+b
        a=b
        b=c 
        print(c)

fib(4)