#!/usr/bin/env python3

import sys
import csv
import math
import os.path

DEBIT_TRANSACTION_NAMES = ["amount", "debit"]


def roundup():
    pass


def string_to_money_int(number):
    if number.find(".") != -1:
        decimals = len(number)-1-number.find(".")
        if decimals >= 3:
            number = number[:-decimals+2]
        return int(number.replace(".", ""))


def get_roundups_in_csv(csv_file_name):
    with open(str(csv_file_name), "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        csv_list = list(csv_reader)
        head = csv_list[0]
        head = [item.lower() for item in head]
        possible_amount_column = None
        for possibility in DEBIT_TRANSACTION_NAMES:
            if possibility in " ".join(head):
                possible_amount_column = possibility
                exit

        if possible_amount_column == None:
            print("No column for transactions found.")
            exit()

        amount_column = head.index(possible_amount_column)

        del csv_list[0]

        total = 0

        for transaction in csv_list:
            if transaction[amount_column] == "":
                continue
            transaction = string_to_money_int(transaction[amount_column])
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
Usage: roundup <directory or file.csv>

Not providing a path means the program will loop through the current directory.

Examples:
    Round up chase.csv               :  roundup chase.csv
    Round up transactions directory  :  roundup transactions
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

if __name__ == "__main__":
    roundup()
