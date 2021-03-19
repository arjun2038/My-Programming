a1 = {'a':2, 'b':31, 'd':4, 'c':22, 'e':30}
a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
a1_sorted_keys_2 = sorted(a1, key=a1.get)
print("Decending Order")
print(a1_sorted_keys)
print("Ascending Order")
print(a1_sorted_keys_2)

