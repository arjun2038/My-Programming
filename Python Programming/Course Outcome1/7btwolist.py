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
for i in range(num2):
    list2.append(int(input()))
for i in range(len(list1)):
    sum1+=list1[i]
for i in range(len(list2)):
    sum2+=list2[i]
if sum1==sum2:
    print("The sum is "+str(sum1)+" is same in both list")
else:
    print("The sum of first list is "+str(sum1)+" and the sum of second list is"+str(sum2))