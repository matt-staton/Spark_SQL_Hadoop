#!/usr/bin/python
import sys

#create empy dictionary
reverse_index = {}

# input comes from STDIN
#Example input
#From: jane.tholt@enron.com	<23551738.1075857497351.JavaMail.evans@thyme>
#To: outlook.team@enron.com	<23551738.1075857497351.JavaMail.evans@thyme>
#From: jane.tholt@enron.com	<23426663.1075857497542.JavaMail.evans@thyme>
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # parse input from mapper
    email, idd = line.split('\t')   #id will be a list if it has multiple instances

    # convert to string
    try:
        email = str(email)
		idd = str(idd)
		
    except ValueError:
        continue


    try:
		reverse_index[email] = reverse_index[email].append(idd)

	except:
        reverse_index[email] = [idd]

	# write the tuples to stdout
for email in reverse_index.keys():
    print '%s\t%s' % (email, reverse_index[email])