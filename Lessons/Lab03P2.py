length = float(input("Please enter room length: "))
width = float(input("Please enter the room width: "))
height = float(input("Please enter the room height: "))
btuNeeded = length*width*height*3.5
sun= input("Does the room get a lot of sunlight? Yes or no: ")
if sun == "yes":
    btuNeeded=btuNeeded*1.2
print("The amount of BTU needed is ", btuNeeded)
