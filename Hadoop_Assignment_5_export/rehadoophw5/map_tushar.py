import sys

def read_input(file):
	for line in file:
		yield line.strip()


#out format: sess count, click event count, contact form, SRP, VDP

# process imps: notice, I've printed an i at the end to identify
# that this line came from imps data
def process_imps(line):
	# this line is from the impressions file
	# pull out the vin, the srp count, vdp count from this line
	print '%s\t%s\ti'%(vin, [0,0,0,srp,vdp])

# process sess: notice, I've printed an s at the end to identify
# that this line came from session data
def process_sess(line):
	# this line is from the impressions file
	# pull out the vins, and all the other counts for all
	# vehicles and print them 
	
	# output_data: {vin: [x,y,z,0,0]}
	for vin in output_data:
		print '%s\t%s\ts'%(vin, output_data[vin])

for line in read_input(sys.stdin):
	if line.count(',')==2:
		# if there are 2 commas, it is an impression
		process_imps(line)
	else:
		# otherwise, it is a session
		process_sess(line)
