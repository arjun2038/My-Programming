newlist=[]
list=[]
n = int(input("Enter the number of numbers to enter"))
for i in range(n):
    list.append(int(input()))
print("The list is")
print(list)
print("The list of positive numbers")
for i in range(n):
    if list[i]>0:
        newlist.append(list[i])
print(newlist)
