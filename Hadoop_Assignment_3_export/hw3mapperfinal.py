#!/usr/bin/python
import sys
import re


for line in sys.stdin:   
        
    line = str(line)
    #Regex - find only text left of "X-To:"
    mystr = re.search(r'(^.*)(X-To:).*', line)    #Cannot have spaces in RegEx!!!!!!!!!!!!!!!
        
    line = mystr.group(1)		#This is everything left of X-to
        
    line = re.split(r'\t+', line)  #list of header topics for 1 email
		
	m_id = re.search(r'(^.*)(<.*>)(.*)', line[0])    # Isolate email id and keep from, to, etc...
    
	line[0] = m_id.group(2)
			
	
	print '%s\t%s' % (line[2], line[0])
	print '%s\t%s' % (line[3], line[0])