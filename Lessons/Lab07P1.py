def main():
    bmiq()
    bpq()

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
