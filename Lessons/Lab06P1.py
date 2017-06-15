houseNum = int(input("How many houses were sold? "))
housePrice = []
commission = []
for i in range(0,houseNum):
    price = int(input("Please enter the price of the house:"))
    housePrice.append(price)
for i in range(0, houseNum):
    comm = housePrice[i]*.03
    commission.append(comm)
    print("the house price is", housePrice[i], "and the commission was", commission[i])
