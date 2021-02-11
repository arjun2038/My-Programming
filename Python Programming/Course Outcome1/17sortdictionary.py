import operator
a = {3: 10, 1: 3, 0: 6, 2: 5}
print("The dictionary is\n")
print(a)
print("\nDictionary in Ascending order\n")
print(sorted(a.items(),key=operator.itemgetter(1)))
print("\nThe Dictionary in Decending order\n")
print(sorted(a.items(),key=operator.itemgetter(1),reverse=True))
