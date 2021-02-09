a=[]
list=[]
n=int(input("Enter the number of numbers to enter"))
for i in range(n):
    x=int(input())
    if x<=100:
        list.append(x)
    else:
        list.append("over")
print(list)



