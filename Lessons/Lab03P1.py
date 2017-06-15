midterm = float(input("Please enter midterm score: "))
final = float(input("Please enter final score: "))
improvement = final - midterm
endGrade = midterm + final
print("Your final score is ", endGrade, "!")
if improvement > 20:
    print("Good job on the improvement! Here have a 5 points")
    endGrade = endGrade + 5
    print("Your new grade is ", endGrade, "!")
else:
    print("Lrn 2 school, noob")
