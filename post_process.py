import csv
import os
from datetime import datetime

FOLDER = 'data'

def string_to_time(string):
    year, month, day = string.split('/')
    return datetime(int(year) + 1911, int(month), int(day))

def is_same(row1, row2):
    if not len(row1) == len(row2):
        return False

    for index in range(len(row1)):
        if row1[index] != row2[index]:
            return False
    else:
        return True

def main():
    file_names = os.listdir(FOLDER)
    for file_name in file_names:
        if not file_name.endswith('.csv'):
            continue

        rows = []
        dates = []

        # Load and remove duplicates (use newer)
        with open('{}/{}'.format(FOLDER, file_name), 'rb') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    index = dates.index(row[0])
                except ValueError:
                    rows.append(row)
                    dates.append(row[0])
                else:
                    rows[index] = row

        # Sort by date
        rows.sort(key=lambda x: string_to_time(x[0]))

        with open('{}/{}'.format(FOLDER, file_name), 'wb') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

if __name__ == '__main__':
    main()