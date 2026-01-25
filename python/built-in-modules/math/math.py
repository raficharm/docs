import math

choice=input(" do you want to use radian or degree? \n 1. Degree \n 2. Radian \n ")
if choice=='Degree':
    x=float(input("Enter x in Degree : "))
    x = (x * 180)/math.pi

elif choice=='Radian':
    x=float(input("Enter x in radian : "))
else:
    print('Invalid Option')
    exit()


deg =(x * 180)/math.pi
print(f'x in degree is {deg}')
print(f'acos(x) is {math.acos(x)}')
print(f'asin(x) is {math.asin(x)}')
print(f'atan(x) is {math.atan(x)}')
print(f'tan2(x) is {math.atan2(x)}')
print(f'atanh(x) is {math.atanh(x)}')
print(f'cell(x) is {math.celi(x)}')
print(f'comb(9,7) is {math.comb(9,7)}')
print(f'acos(x) is {math.acos(x)}')
print(f'cos(x) is {math.cos(x)}')
print(f'acosh(x) is {math.acosh(x)}')
print(f'x in degree is {math.degrees(x)}')
print(f'factorial(34) is {math.factorial(34)}')
print(f'floor(x) is {math.floor(x)}')
print(f'gamma(x) is {math.gamma(x)}')
print(f'gcd(6,9) is {math.gcd(6,9)}')
.
.
. 

"'Just type python -m pydoc math '" :(


