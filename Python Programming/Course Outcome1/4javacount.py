res=[]
lineoftext=input("Enter The Line Of Text")
list=lineoftext.split(" " or "," or ".")
for i in range(len(list)):
    list.count(list[i])
print(list.count(list[i]))
for i in list:
    if i not in res:
        res.append(i)
for i in range(len(res)):
    print("%s = %s times present" % (res[i], list.count(res[i])))

