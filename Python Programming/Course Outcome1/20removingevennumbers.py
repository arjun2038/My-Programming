list1=[]
list=[1,2,3,5,9,7,8,16,15,17,19,23,26]
for i in range(len(list)):
    if(list[i]%2==1):
        list1.append(list[i])
print("The list of non-positive numbers")
print(list1)