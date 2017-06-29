scores = []
scoreLen = len(scores)

for i in range (0,7):
    score = int(input("Give a students test score:"))
    scores. append(score)
print(scores)
scores.sort()
print("The highest score is:" ,scores[-1])

passScores =[]
i = 0
for i in scores:
    if i >= 70:
        passScores.append(i)

passnum = len(passScores)
print("The list of passing scores is:" ,passScores, "and the total number of those who passed is", passnum)

for i in range(0,7):
    scores[i] = scores[i]+5

print("You get 5 points, and you get 5 points, EVERYONE GETS 5 POIIIIIIINTS!!!!!")
print("The new dummy-curved list is:" ,scores)
