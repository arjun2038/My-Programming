#Write a Python program to read a file line by line and store it into a list
fr = open("sample.txt",'r')
str1 = fr.readlines()
print(str1)