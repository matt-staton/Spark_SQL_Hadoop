#!/usr/bin/python


import sys
import csv

event_field_list = [ 'timestamp', 'event_action', 'event_target', 'vin' ]
vin_field_list = [ 'condition', 'year', 'make', 'model', 'price', 'mileage' ]

def read_session(file):
    for line in file:
        try:
            # split the line into components: user_id:sessions_type, event_list, in dictionary
            yield line.strip().split('\t')
        except:
            #split on commas for csv file of impressions
            yield line.strip().split(',')
            
def main(file9):
              #loop for session data
	for user_id_string, event_list_string, vin_dict_string in read_session(file9):
        user_id, session_type = user_id_string.split(':')
        event_list = eval(event_list_string)
        vin_dict = eval(vin_dict_string)
        #print '{}:{}\t{}\t{}'.format(user_id, session_type, event_list, vin_dict)
        seen_vehicles = []
        vehicle_dictionary = {}
		print user_id


if __name__ == "__main__":
    main(sys.stdin)