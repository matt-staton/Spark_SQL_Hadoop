#!/usr/bin/python

# Read session

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
    try:           #loop for session data
        for user_id_string, event_list_string, vin_dict_string in read_session(file9):
            user_id, session_type = user_id_string.split(':')
            event_list = eval(event_list_string)
            vin_dict = eval(vin_dict_string)
            #print '{}:{}\t{}\t{}'.format(user_id, session_type, event_list, vin_dict)
            seen_vehicles = []
            vehicle_dictionary = {}
            for i in event_list:          # here i is each event i['vin'][] is each vin in list
                clicks = 0
                contact = 0
                vin = i['vin']
                event = i['event_target']
                action = i['event_action']
                
                if not (i['vin'] in seen_vehicles):
                    seen_vehicles.append(i['vin']) 

                    if event == 'contact form':
                        contact = 1
                    if action == 'click':
                        clicks = 1
                    
                    vehicle_dictionary[i['vin']] = [i['vin'], 1, clicks, contact,0,0]
                
                else: 
                    if event == 'contact form':
                        contact = 1
                        vehicle_dictionary[i['vin']][3] += 1
                    if action == 'click':
                        clicks = 1  
                        #print vehicle_dictionary[i['vin']]['click count'].values
                        vehicle_dictionary[i['vin']][2] += 1
                        #print vehicle_dictionary[i['vin']]['click count'] 
                        
                    vehicle_dictionary[i['vin']][1] = 1
            
            for x in vehicle_dictionary.keys():
                
                 print(vehicle_dictionary[x])

    except: 
        for line2 in read_session(sys.stdin):
            #print line2
            vinn, kind, cnt = str(line2[0]).strip().split(',')
            cnt = int(cnt)

            if kind == 'VDP':
                print( [vinn,0,0,0, cnt,0] )
            elif (kind == 'SRP'):
                print( [vinn,0,0,0, 0, cnt] )
            else:
                continue
                                
if __name__ == "__main__":
    main(sys.stdin)