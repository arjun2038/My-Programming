new=[]
list=[]
n=int(input("Enter number of names to enter"))
for i in range(n):
    names=(input("Enter the name"))
    new=names.split(" ")
    list.append(new[0])
print("The cllection of first lines are")
print(list)