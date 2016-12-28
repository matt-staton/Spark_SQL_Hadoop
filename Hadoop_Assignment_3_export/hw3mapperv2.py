#!/usr/bin/python
import sys
import re

# --- get all lines from stdin ---
for line in sys.stdin:
	try:
		mystr = re.search(r'(^.*)(X-To:).*', line)    #Cannot have spaces in RegEx!!!!!!!!!!!!!!!
		line1 = mystr.group(1)
    except:
		continue
    
        
    line2 = re.split(r'\t+', line1)   
	
	m_id = re.search(r'(^.*)(<.*>)(.*)', line2[0])    #Cannot have spaces in RegEx!!!!!!!!!!!!!!!
    
    line2[0] = m_id.group(2)
    #mylist.append(line)
	
    # Print the key value pairs
    print '%s\t%s' % (line2[2], line2[0])
    print '%s\t%s' % (line2[3], line2[0])