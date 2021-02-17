def perfectnum(number):
    remain=[]
    sum=0
    for i in range(1,int(number/2)+1):
        if number%i==0:
            remain.append(i)
    for i in range(len(remain)):
        sum=sum+remain[i]
    if int(sum)==number:
        print(str(number)+" is a Perfect Number")
    else:
        print(str(number)+" is not a Perfect Number")
number=int(input("Enter the Number\n"))
perfectnum(number)