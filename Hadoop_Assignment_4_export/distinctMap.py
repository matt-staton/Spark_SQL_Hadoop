#!/usr/bin/python

# Example to compute distinct values in one or more fields
# Here we examine event log entries

import sys

field_name_list = ['user_id', 'event', 'timestamp', 'vin', 'condition', 'year', 'make', 'model', 'price', 'mileage' ]

def read_input(file):
    for line in file:
        # split the line into individual fields (fields are delimited by tab).
        yield line.strip().split('\t')

def main():
    # input comes from STDIN (standard input)
    # data is the generator that produces individual inputs
    data = read_input(sys.stdin)

    for log_entry in data:
        print  '%s\t%d'% ( log_entry[1], 1 )

if __name__ == "__main__":
    main()
