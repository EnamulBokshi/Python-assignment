a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
operation = input("Enter Operation (+,-,*,/): ")
if(operation == '+'):
    result = a+b 
elif operation == '-':
    result = a-b
elif operation == '*':
    reslult = a*b
else:
    result = a/b
print(result)