"""Module to convert the txt files to csv files"""

import csv
import os


def convert_file(file):
    """Opens the file and removes the unwanted strings"""

    dest_file = file.split('.')[0]+'.csv'

    with open(file, 'r', encoding='utf8') as file,\
            open(dest_file, 'w', encoding='utf8') as new_file:
        reader = csv.reader(file, delimiter='\t')
        writer = csv.writer(new_file)

        for row in reader:
            row = [col.strip() for col in row]
            writer.writerow(row)


def main():
    """Main function"""

    files = [file for file in os.listdir('data/')]

    for file in files:
        file = 'data/' + file
        convert_file(file)


if __name__ == "__main__":
    main()
