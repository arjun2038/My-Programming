def paliandrome(string):
    reverse=string[len(string)::-1]
    return reverse
string=input("Enter the string\n")
paliandrome(string)
if paliandrome(string).lower()==string.lower():
    print("It is a Paliandrome")
else:
   print("It is not Paliandrome")