#!/usr/bin/env python3
import argparse
import csv, _csv
import _io

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculates your average marks',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='''
Note: Module Numbers needs to have a space between the number and the course.
Example: EEEE 1028''')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                        help="Use the csv file provided to calculate marks instead")

    return parser.parse_args()

def input_codes(credit) -> list:
    # Getting Codes
    codes = list()
    code = "Dummy"
    while code:
        code = input("Input Module Code (Press Return to Finish): ")
        if not code == '':
            if code not in credit:
                print("Invalid Code, Try Again")
            else:
                if not code in codes:
                    codes.append(code)
                else:
                    print("The code given is already passed in, Try Again")
    return codes

def input_marks(codes: list) -> dict:
    # Getting Marks
    marks = dict()
    for code in codes:
        mark = input(f"Input the mark for module {code}: ")
        marks[code] = int(mark)
    return marks

def get_marks_csv(csvFile: _io.TextIOWrapper) -> dict:
    reader: _csv.reader = csv.reader(csvFile)
    marks: dict = dict()

    for data in reader:
        if not data[0] in marks:
            marks[data[0]] = int(data[1])
        else:
            raise ValueError("Duplicate module code found! Please check your csv file.")
    csvFile.close()

    return marks

def calculate_marks(marks: dict, credit: dict) -> float:
    # Calculating total marks
    totalCredits: int = 0
    totalMarks: float = 0
    for module, mark in marks.items():
        moduleCredit: int = credit[module]
        totalCredits += moduleCredit
        totalMarks += moduleCredit * mark
    totalMarks /= totalCredits

    return totalMarks

def main():
    args = parse_arguments()

    # Loading Credits
    credit = dict()
    with open('credits.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
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

    totalMarks: float = calculate_marks(marks, credit)
    print("Your Marks:", totalMarks)

if __name__ == '__main__':
    main()
