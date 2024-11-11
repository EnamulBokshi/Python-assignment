n = int (input())
def fiboUtil(n,memo):
    if n<=1:
        return n
    if(memo[n] != -1):
        return memo[n]
    memo[n] = fiboUtil(n-1,memo)+fiboUtil(n-2,memo)
    return memo[n]
def nthFibo(n):
    memo = [-1 for x in range(n+1)]
    return fiboUtil(n,memo)
result = nthFibo(n)
print(result)