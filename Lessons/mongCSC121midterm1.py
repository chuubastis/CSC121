
p1 = input("Player one:  please enter r for rock, p for paper, or s for scissors: ")

while p1 != "r" and p1 != "s" and p1 != "p":
    print("Try again dingdong: ")
    p1 = input("Player one:  please enter r for rock, p for paper, or s for scissors: ")

p2 = input("Player one's little brother: please enter r for rock, p for paper, or s for scissors: ")

while p2 != "r" and p1 != "s" and p1 != "p":
    print("Try again dingdong: ")
    p2 = input("Player one's little brother: please enter r for rock, p for paper, or s for scissors: ")

if p1 == "r" and p2 == "r":
    print("Its a tie!")
elif p1 == "r" and p2 == "s":
    print("Player one wins!")
elif p1 == "r" and p2 == "p":
    print("Little brother wins!")
elif p1 == "s" and p2 == "r":
    print("Little brother wins!")
elif p1 == "s" and p2 == "s":
    print("Its a tie!")
elif p1 == "s" and p2 == "p":
    print("Player one wins!")
elif p1 == "p" and p2 == "r":
    print("Player one wins!")
elif p1 == "p" and p2 == "p":
    print("Its a tie!")
elif p1 == "p" and p2 == "s":
    print("Little brother wins!")
else:
    print("You guys are too dumb for this game")
