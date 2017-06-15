copies = float(input("How many copies are you buying? "))
if 1<= copies <=10:
    final = copies*99
    print("The unit price is $99, the final price is $", final)
elif 11<= copies <=50:
    final = copies*89
    print("The unit price is $89, the final price is $", final)
elif 51 <= copies <= 100:
    final = copies*79
    print("The unit price is $79, the final price is $", final)
elif copies >= 101:
    final = copies*69
    print("The unit price is $69, the final price is $", final)
