import csv
import  pandas
with open('meremarks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')

        line_count += 1
        print(f'\t{row[0]}  has {row[1]} marks.')
        line_count += 1

df=pandas.read_csv("meremarks.csv")
print(df)