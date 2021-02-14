for i in range(0,9):
    for j in range(0,5):
        if i < 5:
            if j<=i:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if i+j<=8:
                print("*",end="")
            else:
                print(" ",end="")
    print("\n")
