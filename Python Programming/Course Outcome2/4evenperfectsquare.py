import numbers
lowerrange=int(input("Enter the lowest Range\n"))
highrange=int(input("Enter the Higher Range\n"))
for i in range(lowerrange,highrange+1):
        root=i**(1/2)
        if root.isnumeric()==True:
            print(i)


