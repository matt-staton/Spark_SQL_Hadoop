#!/usr/bin/python

# Read session

import sys

event_field_list = [ 'timestamp', 'event_action', 'event_target', 'vin' ]
vin_field_list = [ 'condition', 'year', 'make', 'model', 'price', 'mileage' ]

def read_session(file):
    for line in file:
        # split the line into components: user_id:sessions_type, event_list, in dictionary
        yield line.strip().split('\t')

def main():
    for user_id_string, event_list_string, vin_dict_string in read_session(sys.stdin):
        user_id, session_type = user_id_string.split(':')
        event_list = eval(event_list_string)
        vin_dict = eval(vin_dict_string)
        # print '{}:{}\t{}\t{}'.format(user_id, session_type, event_list, vin_dict)


if __name__ == "__main__":
    main()
