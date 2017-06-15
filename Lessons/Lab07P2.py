def main():
    print("Enter 1 to calculate BMI only. \nEnter 2 to determine if you have high blood pressure only. \nEnter 3 to do both. ")
    selection = int(input("Enter your choice: "))
    if selection == 1:
        bmiq()
    elif selection == 2:
        bpq()
    elif selection == 3:
        bmiq()
        bpq()
    else:
        print("Don't be jerk and enter a proper answer.")

def bmiq():
    height = int(input("Please enter your height in inches: "))
    weight = int(input("Please enter your weight in pounds: "))
    bmi = (703*weight)/(height*weight)
    print("Your BMI is", bmi)
def bpq():
     sys = int(input("Enter your systolic pressure: "))
     dia = int(input("Please enter your diastolic pressure: "))
     if sys >=140 or dia >= 90:
         print("You have high blood pressure.")
     else:
         print("You do not have high blood pressure.")

main()
