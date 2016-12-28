#!/usr/bin/python


import sys
import csv

event_field_list = [ 'timestamp', 'event_action', 'event_target', 'vin' ]
vin_field_list = [ 'condition', 'year', 'make', 'model', 'price', 'mileage' ]


def read_input(file):
	for line in file:
		yield line.strip()


#out format: sess count, click event count, contact form, SRP, VDP

# process imps: notice, I've printed an i at the end to identify
# that this line came from imps data
def process_sess(line):
               
	user_id_string, event_list_string, vin_dict_string = line.split('\t')
	user_id, session_type = user_id_string.split(':')
	event_list = eval(event_list_string)
	vin_dict = eval(vin_dict_string)
	seen_vehicles = []
	vehicle_dictionary = {}
	#print '{}:{}\t{}\t{}'.format(user_id, session_type, event_list, vin_dict)

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
		
		temp = vehicle_dictionary[x]
		print temp
	
	# this line is from the impressions file
	# pull out the vin, the srp count, vdp count from this line
	#print '%s\t%s\ti'%(vin, [0,0,0,srp,vdp])

# process sess: notice, I've printed an s at the end to identify
# that this line came from session data
def process_imps(line):
	print "imps"
	line = line.split('\t')
	
	vinn, kind, cnt = str(line[0]).strip().split(',')
	cnt = int(cnt)

	if kind == 'VDP':
		print( [vinn,0,0,0, cnt,0] )
	elif (kind == 'SRP'):
		print( [vinn,0,0,0, 0,cnt] )

	
	# this line is from the impressions file
	# pull out the vins, and all the other counts for all
	# vehicles and print them 
	
	# output_data: {vin: [x,y,z,0,0]}
	#for vin in output_data:
		#print '%s\t%s\ts'%(vin, output_data[vin])

for line in read_input(open("dataSet5sessions.tsv", 'r')):
	if line.count(',')==2:
		# if there are 2 commas, it is an impression
		process_imps(line)
	else:
		# otherwise, it is a session
		process_sess(line)