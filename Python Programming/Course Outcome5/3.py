#Write a Python program to read each row from a given csv file and print a list of strings
import csv
lst=[]
f=open("1.csv")
reader=csv.reader(f)
for string in reader:
    lst.append(string)    
f.close()
print(lst)