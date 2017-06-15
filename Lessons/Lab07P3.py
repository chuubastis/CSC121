def main():
    place = input("Are you an instate student? y/n: ")
    hours = int(input("How many credit hours are you taking? "))
    if place == "y":
        tuition_instate(hours)
    elif place == "n":
        tuition_outstate(hours)
    else:
        print("Don't be a noob.")

def tuition_instate(hours):
    if hours <= 12:
        price = 60*hours
    else:
        price = 720
    print("Your tuition is", price)


def tuition_outstate(hours):
    if hours <=15:
        price = 200*hours
    else:
        price = 3000
    print("Your tuition is", price)

main()
