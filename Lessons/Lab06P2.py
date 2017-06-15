spread1 = range(3, 6)
spread2 = range(3,11,3)
spread3 =range(9,3,-2)
spreadlist1 = []
spreadlist2 = []
spreadlist3 = []

for i in spread1:
    spreadlist1.append(i)
for i in spread2:
    spreadlist2.append(i)
for i in spread3:
    spreadlist3.append(i)
masterlist = spreadlist1+spreadlist2+spreadlist3

for i in masterlist:
    print(i)
