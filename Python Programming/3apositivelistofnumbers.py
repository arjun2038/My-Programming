newlist=[]
list=[]
n = int(input("Enter the number of numbers to enter"))
for i in range(n):
    list.append(int(input()))
print(list)
for i in range(n):
    if list[i]>0:
        newlist.append(list[i])
print(newlist)