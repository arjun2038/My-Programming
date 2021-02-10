colorlist=[]
n=int(input("Enter the number of colors to enter\n"))
for i in range(n):
    colorlist.append(input())
print("The first colour in the list is "+colorlist[0])
print("The second colour in the list is "+colorlist[-1])