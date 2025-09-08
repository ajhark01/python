import math

n=int(input("Enter the number: "))
if n<0:
    print ("Not defined for negative numbers: ")
else:
    result = math.sqrt(n)
    print('Square root :', result)
    result = math.log(n)
    print('Logarithm :', result)
    result = math.sin(n)
    print('Sine :', result)

