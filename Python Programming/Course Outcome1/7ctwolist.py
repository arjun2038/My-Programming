list1=[]
list2=[]
sum1=0
sum2=0
num1=int(input("Enter the number of elements in first list"))
print("Enter the elements")
for i in range(num1):
    list1.append(int(input()))
num2=int(input("Enter the number of elements in Second list"))
print("Enter the elements")
for j in range(num2):
    list2.append(int(input()))
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            print(str(list1[i])+" is occur in both list")