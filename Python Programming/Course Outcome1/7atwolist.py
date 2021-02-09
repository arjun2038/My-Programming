list1=[]
list2=[]
num1=int(input("Enter the number of elements in first list"))
print("Enter the elements")
for i in range(num1):
    list1.append(int(input()))
num2=int(input("Enter the number of elements in Second list"))
print("Enter the elements")
for i in range(num2):
    list2.append(int(input()))
if len(list1)==len(list2):
    print("The lists are same")
else:
    print("The size of lists are not same")
