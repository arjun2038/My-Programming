range1=int(input("Enter the rages\n"))
range2=int(input())
root1=int(range1**(1/2))
root2=int(range2**(1/2))
for i in range(root1,root2):
    x=square=i**2
    rem=square%10
    if rem==4 or rem==0:
        square = square // 10
        rem=square%10
        if rem==0 or rem==2 or rem==4 or rem==6 or rem==8:
            square = square // 10
            rem = square % 10
            if rem==0 or rem==2 or rem==4 or rem==6 or rem==8:
                square = square // 10
                rem = square % 10
                if rem==0 or rem==2 or rem==4 or rem==6 or rem==8:
                    square = square // 10
                    rem = square % 10
                    if rem==0 or rem==2 or rem==4 or rem==6 or rem==8:
                        print(x)





