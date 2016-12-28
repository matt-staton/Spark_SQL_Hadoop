#!/usr/bin/python
import sys
import re


def regex_manip(line1):    
    
	#for line in file:     
    #line = str(line)
    #Regex - find only text left of "X-To:"
		try:
			mystr = re.search(r'(^.*)(X-To:).*', line1)    #Cannot have spaces in RegEx!!!!!!!!!!!!!!!
			line1 = mystr.group(1)
        except:
			continue
    
        
    return re.split(r'\t+', line1)
		
		


# --- get all lines from stdin ---
for line in sys.stdin:
    
	line = regex_manip(line)
   
    m_id = re.search(r'(^.*)(<.*>)(.*)', line[0])    #Cannot have spaces in RegEx!!!!!!!!!!!!!!!
    
    line[0] = m_id.group(2)
    #mylist.append(line)
	
    # Print the key value pairs
    print '%s\t%s' % (line[2], line[0])
    print '%s\t%s' % (line[3], line[0])