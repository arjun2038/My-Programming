string=input("Enter the string")
print("The output string is given below")
if string[-3:]=="ing":
    print(string[:-3]+"ly")
else:
    print(string+"ing")