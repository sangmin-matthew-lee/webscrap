def plus(a,b):
    return (a + b)

def sub(a,b):
    return (a-b)

def multiple(a,b):
    return (a*b)

def div (a,b):
    return (a/b)

def pow(a,b):
    return (a**b)

def rem(a,b):
    return (a%b)

def neg(a):
    return (-a)

def printNum(val):
    print(f"Calculated Value is: {val}")

sum = plus(2,5)
subtraction = sub(3,1)
multi = multiple(2,5)
divide = div(5,2)
reminder = rem(3,2)
power = pow(2,5)
negative = neg(2)

printNum(sum)
printNum(subtraction)
printNum(multi)
printNum(divide)
printNum(reminder)
printNum(power)
printNum(negative)