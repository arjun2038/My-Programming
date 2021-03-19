import csv
with open('arjun.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


with open('arjun.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
