# CSV-RoundUps [![PyPI](https://img.shields.io/pypi/v/roundup-csv.svg)](https://pypi.org/project/roundup-csv/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/roundup-csv.svg)](https://pypi.org/project/roundup-csv/)
I tried Acorns and Stash and didn't want to pay monthly, so I made this python script to "round-up" transactions.

```
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
```