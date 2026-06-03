# def fib(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     return fib(n-1)+fib(n-2)

n=int(input("enter a num : "))
# print(fib(n))    



def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

print(fibonacci(n))