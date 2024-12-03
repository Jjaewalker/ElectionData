#installreadfiles
import csv
import os
import pandas as pd

#Openthecsvfile

#with open('../HoC-GE2024-results-by-constituency.csv', mode='r') as file:
#    # Create a CSV reader object
#    csv_reader = csv.reader(file)
#
#    # Read the header
#    header = next(csv_reader)
#    print(f"header: {header}")
#
#    # Read each row of the CSV file
#    for row in csv_reader:
#        print(f"Row:  {row}")

file_path = 'FullDataFor2024.csv'

try:
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        print(f"Row {index}:", dict(row))

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error reading file: {str(e)}")
