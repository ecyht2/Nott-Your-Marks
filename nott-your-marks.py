#!/usr/bin/env python3
import argparse
import csv, _csv

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculates your average marks')
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

    # Getting Codes
    codes: list = input_codes(credit)
    # Getting Marks
    marks: dict = input_marks(codes)

    totalMarks: float = calculate_marks(marks, credit)
    print("Your Marks:", totalMarks)

if __name__ == '__main__':
    main()
