#!/usr/bin/env python3
"""Calculates the average marks for your modules."""
import argparse
import csv
import _csv
import _io

def parse_arguments():
    """Create an argparse instance."""
    parser = argparse.ArgumentParser(description='Calculates your average marks',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='''
Note: Module Numbers needs to have a space between the number and the course.
Example: EEEE 1028''')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                        help="Use the csv file provided to calculate marks instead")

    return parser.parse_args()

def input_codes(credit) -> list:
    """Get the module codes using stdin."""
    # Getting Codes
    codes = []
    code = "Dummy"
    while code:
        code = input("Input Module Code (Press Return to Finish): ")
        if not code == '':
            if code not in credit:
                print("Invalid Code, Try Again")
            else:
                if code not in codes:
                    codes.append(code)
                else:
                    print("The code given is already passed in, Try Again")
    return codes

def input_marks(codes: list) -> dict:
    """Get the marks for each modules using stdin."""
    # Getting Marks
    marks = {}
    for code in codes:
        mark = input(f"Input the mark for module {code}: ")
        marks[code] = int(mark)
    return marks

def get_marks_csv(csv_file: _io.TextIOWrapper) -> dict:
    """Get the marks and it's corresponding module code from csv_file."""
    reader: _csv.reader = csv.reader(csv_file)
    marks: dict = {}

    for data in reader:
        if not data[0] in marks:
            marks[data[0]] = int(data[1])
        else:
            raise ValueError("Duplicate module code found! Please check your csv file.")
    csvFile.close()

    return marks

def calculate_marks(marks: dict, credit: dict) -> float:
    """Calculates the average marks."""
    # Calculating total marks
    total_credits: int = 0
    total_marks: float = 0
    for module, mark in marks.items():
        module_credit: int = credit[module]
        total_credits += module_credit
        total_marks += module_credit * mark
    total_marks /= total_credits

    return total_marks

def main():
    """Main function."""
    args = parse_arguments()

    # Loading Credits
    credit = {}
    with open('credits.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for data in reader:
            credit[data["Code"]] = int(data["Credit"])

    # If filed is passed
    if not args.file:
        # Getting Codes
        codes: list = input_codes(credit)
        # Getting Marks
        marks: dict = input_marks(codes)
    else:
        marks = get_marks_csv(args.file)

    total_marks: float = calculate_marks(marks, credit)
    print("Your Marks:", total_marks)

if __name__ == '__main__':
    main()
