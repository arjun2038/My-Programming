string=input("Enter the string")
string=string[-1]+string[1:(len(string)-1)]+string[0]
print("String after exchanging first and last letter\n"+string)