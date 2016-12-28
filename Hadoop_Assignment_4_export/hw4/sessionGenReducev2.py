#!/usr/bin/python

# Reducer for session generation.
# Here we assemble user sessions

import sys

def read_key_value(file):
    for line in file:
        # split the line into components, before and after the tab
        yield line.strip().split('\t', 1)

def session_classify(session):
    for i in session:
        if i['event_target'] == "contact form":
            return 'submitter'
        elif i['event_action'] == 'click':
            return 'clicker'
        elif i['event_action'] == 'show' or i['event_action'] == 'display':
            return 'shower'
        elif i['event_action'] == 'visit':
            return 'visitor'
        else:
            return 'other'
    
def get_cars_viewed(event_list):
    seen_vehicles = []
    vehicle_dictionary = {}
    for i in event_list:
        if not (i['vin'] in seen_vehicles):
            seen_vehicles.append(i['vin'])
            vehicle_dictionary[i['vin']] = {'condition':i['condition'], 'year':i['year'], 'make':i['make'], 'model':i['model'], 'price':i['price'], 'mileage':i['mileage']}
    return vehicle_dictionary

def main():
    current_user_id = None
    event_list = []

    for user_id, event_string in read_key_value(sys.stdin):
        # eval() converts a data structure described on a string
        # into that internal data structure (for example, a dictionary).
        event = eval(event_string)
        
        # Assemble
        if user_id == current_user_id:
            event_list.append(event)
            continue
        else:
            if current_user_id:
                classification = session_classify(event_list)
                cars_viewed = get_cars_viewed(event_list)
                for i in event_list:
                    i.pop('condition')
                    i.pop('year')
                    i.pop('make')
                    i.pop('model')
                    i.pop('price')
                    i.pop('mileage')
                    i.pop('user_id')
                print '{}:{}\t{}\t{}'.format(current_user_id, classification, event_list, cars_viewed)
            current_user_id = user_id
            event_list = [event]

    if user_id == current_user_id:
        classification = session_classify(event_list)
        cars_viewed = get_cars_viewed(event_list)
        for i in event_list:
            i.pop('condition')
            i.pop('year')
            i.pop('make')
            i.pop('model')
            i.pop('price')
            i.pop('mileage')
            i.pop('user_id')
        print '{}:{}\t{}\t{}'.format(current_user_id, classification, event_list, cars_viewed)

if __name__ == "__main__":
    main()
