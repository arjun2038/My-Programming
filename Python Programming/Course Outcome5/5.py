#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file 
#read the CSV file and display the content
import csv
csv_columns = ['No','Name','Place']
dict_data = [
{'No': 1, 'Name': 'Ali', 'Place': 'Kochi'},
{'No': 2, 'Name': 'Baraman', 'Place': 'Trivandrum'},
{'No': 3, 'Name': 'Jake', 'Place': 'Kollam'},
{'No': 4, 'Name': 'Fedy', 'Place': 'Kannur'},
{'No': 5, 'Name': 'Shaad', 'Place': 'Kozhikode'},
]
csv_file = "names.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)


with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0]+" "+row[1]+" "+row[2])