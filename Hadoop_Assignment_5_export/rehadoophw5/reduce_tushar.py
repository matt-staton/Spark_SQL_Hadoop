import sys
from operator import add

def read_input(file):
	for line in file:
		yield line.strip()


#out format: sess count, click event count, contact form, SRP, VDP

sess_dict, imp_dict, final_dict={}, {}, {}
for line in read_input(sys.stdin):
	
	# pull out the vin, the data, and the 's' or 'i' we appended
	# earlier in the mapper
	vin, data, dat_type=line.split('\t')
	
	if dat_type=='s':
		# process session data
		# add up all the required elements
	elif dat_type=='i':
		# process impression data
		# add up all the required elements

# iterate over final_dict and print the required info
for vin in final_dict:
	print '%s\t%s'%(vin, final_dict[vin])
