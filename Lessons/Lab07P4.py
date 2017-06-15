def main():
    age = float(input("Please enter your age: "))
    rhr = float(input("Please enter your resting heart rate: "))
    heart_rate_calculator(age,rhr)

def heart_rate_calculator(age, rhr):
    thr = (220-age-rhr)*0.4+rhr
    print("Your target heart rate is", thr)

main()
