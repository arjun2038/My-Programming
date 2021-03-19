import csv
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'Sachin', 'Country': 'India'},
{'No': 2, 'Name': 'Broad', 'Country': 'England'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'Australia'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
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
        print(row)
