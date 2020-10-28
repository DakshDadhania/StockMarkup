
import csv

def table():
    with open('dump.csv', newline='') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            print (', '.join(row))
    for i in range(1,1000000000):
        row_list = [ [i, "Linus Torvalds", "Linux Kernel"]]
    with open('dump.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

