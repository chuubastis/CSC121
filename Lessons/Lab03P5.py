customerType = input("Are you a residential or business customer? ")
usage= float(input("How many gallons of water were used? "))
if customerType == "residential":
    if usage <= 8000:
        cost = .004*usage
    elif usage > 8000:
        diff = usage-8000
        cost= diff*.007 + 32
if customerType == "business":
    if usage <=10000:
        cost = .005*usage
    elif usage > 10000:
        diff = usage-10000
        cost = diff*.009 + 50
print("Your final bill is $", cost)
