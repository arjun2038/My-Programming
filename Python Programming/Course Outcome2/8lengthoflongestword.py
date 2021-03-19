list=[]
n=int(input("How many words want to enter"))
print("Enter the word")
for i in range(n):
    list.append(len(input()))
print("The longest word has size "+str(max(list)))

