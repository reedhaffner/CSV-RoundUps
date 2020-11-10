import sys
import csv
import math
import os.path


def get_roundups_in_csv(csv_file_name):
    with open(str(csv_file_name), "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        csv_list = list(csv_reader)
        head = csv_list[0]
        head = [item.lower() for item in head]
        amount_column = head.index("amount")

        del csv_list[0]

        total = 0

        for transaction in csv_list:
            transaction = int(transaction[amount_column].replace(".", ""))
            if transaction < 0:
                continue
            rounded_num = math.ceil(transaction / 100.0)*100
            total += rounded_num - transaction

        return total


def money_int_to_decimal_string(number):
    return str(number)[:-2] + "." + str(number)[-2:]


try:
    directory_or_file = sys.argv[1]
except:
    directory_or_file = "."

if(directory_or_file == "-h"):
    print("""
CSV-RoundUps
---
This is meant to be used with your bank/credit card statements in a CSV format.

It will calculate all of the purchases, round them to the nearest dollar
and give you that total. You can use that total to invest, or save.
---
Usage: python roundup.py <directory or file.csv>

Not providing a path means the program will loop through the current directory.

Examples:
    Round up chase.csv               :  python roundup.py chase.csv
    Round up transactions directory  :  python roundup.py transactions
          """)

if(os.path.isfile(directory_or_file)):
    rounded = get_roundups_in_csv(directory_or_file)
    print(f'{directory_or_file} transactions round to ${money_int_to_decimal_string(rounded)}')
elif(os.path.isdir(directory_or_file)):
    roundups = {}
    for file in os.listdir(directory_or_file):
        if file[-4:] == ".csv":
            roundups[file] = get_roundups_in_csv(file)

    if len(roundups) == 0:
        print("No CSV files found!")
        exit()

    for item in roundups:
        print(
            f'{item} transactions round to ${money_int_to_decimal_string(roundups[item])}')
    print(f'Total is ${money_int_to_decimal_string(sum(roundups.values()))}')