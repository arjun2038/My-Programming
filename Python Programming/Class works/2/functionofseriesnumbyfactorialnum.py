# sum of n terms in the series 1+2/fact(2)+3/fact(3)+......
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=i*fact
    return fact
sum=0
n=int(input("Enter the number of terms want to add"))
for j in range(1,n+1):
    factorial(j)
    sum=(j/factorial(j))+sum
print("The Sum is:"+str(sum))