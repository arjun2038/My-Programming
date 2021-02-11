list = []
colorlist1 = []
n = int(input("Enter the number of colors to in list one\n"))
for i in range(n):
    colorlist1.append(str(input()))
colorlist2 = []
m = int(input("Enter the number of colors to enter\n"))
for j in range(m):
    colorlist2.append(str(input()))
for i in colorlist1:
    if i in colorlist2:
        colorlist1.remove(i)
print("The list of colors present in first list and which is not present in second list  "+str(colorlist1))
