string=input("Enter the string")
first=string[0]
string=string.replace(first,"$")
string=first+string[1:]
print("The modified string is\n"+string)