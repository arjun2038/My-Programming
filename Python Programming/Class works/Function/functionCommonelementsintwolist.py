def intersection(list1,list2):
    interse = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                interse.append(list1[i])
    print("The Elements Common in two Lists")
    print(interse)
list1=[1,3,5,7,9,10,12,23]
list2=[1,2,3,4,5,6,7,8,23]
intersection(list1,list2)
