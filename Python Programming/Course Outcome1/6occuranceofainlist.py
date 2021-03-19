names = input("Enter the name seperated by a comma:")
x = names.split(",")
c = 0
print("x =",x)
for i in x:
    for n in i:
        if n == 'a':
            c = c + 1
print("Counts of 'a':",c)
