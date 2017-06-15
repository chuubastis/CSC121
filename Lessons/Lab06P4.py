amyList= []
bethList= []
connieList= []

amy1 = input("Please enter Amy's first score: ")
amyList.append(amy1)
amy2 = input("Please enter Amy's second score: ")
amyList.append(amy2)
beth1 = input("Please enter Beth's first score: ")
bethList.append(beth1)
beth2 = input("Please enter Beth's second score: ")
bethList.append(beth2)
connie1 = input("Please enter Connie's first score: ")
connieList.append(connie1)
connie2 = input("Please enter Connie's second score: ")
connieList.append(connie2)

scores = [amyList, bethList, connieList]

print("Scores for Amy: ")
for i in scores[0]:
    print(i)
print("Scores for Beth: ")
for i in scores[1]:
    print(i)
print("Scores for Connie: ")
for i in scores[2]:
    print(i)




