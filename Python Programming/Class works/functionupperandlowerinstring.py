def upperl(string):
    f=0
    e=0
    for i in range(len(string)):
        if string[i].islower() == True:
            lower.append(string[i])
            f=f+1
        elif string[i].isupper() == True:
            upper.append(string[i])
            e=e+1
    print("upper case letter are:",e)
    print("The Capital letters in the string are")
    print(upper)
    print("lower case letter are:",f)
    print("The small letters in the string are")
    print(lower)

lower=[]
upper=[]
string=input("Enter the string")
upperl(string)