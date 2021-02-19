print("The Armstrong Numbers between 1 and 500")
for i in range(1,500):
    count=0
    rem=0
    res=0
    num=i
    while num!=0:
        rem=num%10
        num=num//10
        count=count+1
    num=i
    while num!=0:
        rem=num%10
        num=num//10
        res=res+(rem)**count
    if i==res:
       print(str(i)+",",end="")