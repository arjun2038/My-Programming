list=[]
word=input("Enter the String")
for i in range(len(word)):
    list.append(ord(word[i]))
print(list)