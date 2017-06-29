import math
a = int(input("Please enter a number: "))
b = int(input("Please enter another number:  "))
c = int(input("One more number: "))
add = a+b+c
avg = round(add/3, 1)
high = max(a, b, c)
low = min(a, b, c)
pos = 0
neg = 0
print("The sum of the numbers is ", add,", the average is ",avg, ", the highest number is ",high,", the lowest number is",low)

if (a % 2 ==0):
    print("This number is even: ", a)
else:
    print(a, " is an odd number")

if (b % 2 ==0):
    print("This number is even: ", b)
else:
    print(b, " is an odd number")

if (c % 2 ==0):
    print("This number is even: ", c)
else:
    print(c, " is an odd number")

if (a>1):
    pos = pos+1
else:
    neg = neg+1

if (b>1):
    pos = pos+1
else:
    neg = neg+1

if (c>1):
    pos = pos+1
else:
    neg = neg+1

print("The number of positive numbers is ", pos, " and the number of negative numbers is ",neg)
