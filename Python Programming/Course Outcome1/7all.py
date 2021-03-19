list1 = [2, 4, 9, 8, 3, 0]
list2 = [4, 6, 11, 2, 0, 5, 3]
print("list1=", list1)
print("list2=", list2)
a = len(list1)
b = len(list2)

if a == b:
    print("THE LISTS HAVE SAME LENGTH")
else:
    print("THE LISTS HAVE DIFFERENT LENGTH")

s1 = sum(list1)
s2 = sum(list2)
if s1 == s2:
    print("THE TWO LISTS HAVE THE SAME SUM ")
else:
    print("SUM IS NOT SAME")

list1 = set(list1)
list2 = set(list2)
i = list1.intersection(list2)
i = list(i)
print("Common values:", i)
