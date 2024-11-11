n = int(input())
temp  = n
result = 0
while n!=0:
    digit = n%10
    result += digit**3
    n = int(n/10)

if(result == temp):

    print("Yes, The number is Armstrong")
else:
    print("NO, The number is not an Armstrong number")
print("Calulated result is: ",result)