import random
array = []
a = 25
b = 75
x = random.randint(a,b)

j = 0
size = 25
while (j < size):
    x = random.randint(a,b)
    array.append(x)
    j = j+1
print("array ==", array)


sum = 0
for k in array:
    sum = sum + k
length = len(array)
avg = sum/length
print("The average is",avg)

odd = []
even = []
for o in array:
    if o %2 == 0:
        even.append(o)
    else:
        odd.append(o)
print("The number of even numbers is", len(even), "and the number of odd numbers is", len(odd))


array.sort()
print("The median is", array[12])

print("The numbers less than the median are:", array[:11])
print("The numbers greater than the median are:", array[13:])

select = int(input("Please give an integer:"))
count = array.count(select)

if select in array:
    print("This number is in the array",count, "times")
else:
    print("This number is not in the array")

