price1 = 5
price2 = 4
price3 = 2
time = int(input("Please enter the number of minutes parked: "))
hours = int((time/60) + (time%60>0))

if time <= 60:
    price = 5
elif time >60 and time <= 300:
    price = hours * price2
else:
    price = hours * price3

print("Your cost is going to be",price)
