start=int(input("Enter the Starting Year"))
end=int(input("Enter the Ending Year"))
print("The leap years from "+str(start)+" to "+str(end)+" are ")
if start<end:
    for i in range(start,end+1):
        if i%4==0:
            print(i)