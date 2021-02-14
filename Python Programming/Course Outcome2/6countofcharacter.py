list=[]
lenlist=[]
size=0
lenlist=[]
string=input("Enter the string\n")
for i in range(len(string)):
    list=string.split()
for i in range(len(list)):
    lenlist.append(len(list[i]))
    size+=lenlist[i]
print("The number of characters in the above string is "+str(size))
