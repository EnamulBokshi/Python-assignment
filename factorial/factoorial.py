n = int(input())

def factorial(n):
    if(n==1):
        return n
    return n*factorial(n-1)

fact = factorial(n)
print(fact)