import cmath
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def findQuadratic(a,b,c):
    if a == 0:
        return "Linear function"
    d = b*b - 4*c*a
    if d<0:
        print("Complex")
        x1 = (-b+cmath.sqrt(d))/(2*a)
        x2 = (-b-cmath.sqrt(d))/(2*a)
        return [x1,x2]
    if d == 0:
        x = -b/(2*a)
        return x
    x1 = (-b+cmath.sqrt(d))/(2*a)
    x2 = (-b-cmath.sqrt(d))/(2*a)
    return [x1,x2]
result = findQuadratic(a,b,c)
print(result)