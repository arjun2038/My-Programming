vow=[]
string=str(input("Enter the String"))
for i in range(len(string)):
    if (string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u"):
        vow.append(string[i])
print(vow)