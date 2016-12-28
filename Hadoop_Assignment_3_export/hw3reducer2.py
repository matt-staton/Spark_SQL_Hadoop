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
    email, id = line.split('\t')

    # convert to string
    try:
        email = str(email)
		id = str(id)
		
    except ValueError:
        continue

	try:
		if email in reverse_index:
			vals = reverse_index[email]
			#vals is a list of unknow length
			
	except:
		try:
			reverse_index[email] = reverse_index[email].append(id)
		except:
			reverse_index[email] = [id]

# write the tuples to stdout
for email in reverse_index.keys():
    print '%s\t%s' % (email, reverse_index[email][0])