def main():
    scorelist = []
    i=0
    while i<=4:
        score = int(input("Please enter a score: "))
        scorelist.append(score)
        i=i+1
    score_calculator(scorelist)

def score_calculator(scorelist):
    avg = sum(scorelist)/5
    print(avg)



main()
