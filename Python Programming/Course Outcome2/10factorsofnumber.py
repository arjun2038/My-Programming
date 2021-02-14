list=[]
number=int(input("Enter the number for finding factors"))
for i in range(1,int((number/2)+1)):
    if number%i==0:
        list.append(i)
list.append(number)        
print("The list of factors of the number "+str(number))
print(list)
