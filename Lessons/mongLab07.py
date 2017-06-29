a = [ "Euclid", "Archimedes", "Newton","Descartes", "Fermat", "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Nash"]
j = 0

maxlen =0
for k in a:
    if len(a[j])> maxlen:
        maxlen = len(a[j])
        t = a[j]
    j = j+1
print(t, "max length is ", len(t) )

print("The shortest name is:", min(a, key=len))

for i in a:
    print(i[0].upper(),end=' ' )
print()


for u in a:
    print(u[-1].upper(),end=' ')
print()


string = " ".join(a).lower()
char = input("Please enter a lowercase letter: ")
count = string.count(char)
print(char, "appears", count, "times")

list.sort(a)
print(a)
