#!/usr/bin/python
import sys
import ast

def read_key_value(file2):
    for line3 in file2:
        #line3 = ast.literal_eval(line3)
        yield line3 #Read in a string and interpret as a list so we can find our items


vindict={}
def main(file10):
    data = read_key_value(file10)

    #Read one line at a time 
    for m in data:
        #print m
        m = ast.literal_eval(m)#Read in a string and interpret as a list so we can find our items
        #print m
        vin2 = m[0]
        session_count = m[1]
        click_event_count = m[2]
        event_bool_count = m[3]
        count_vdp = m[4]
        count_srp  = m[5]
        #current_vin = None
        
        #Put everything except the vin in a list
        dlist = [session_count,click_event_count,event_bool_count,count_vdp,count_srp]    
        #print dlist
        #Check and see if we've seen this vin before
        if vin2 in vindict.keys():
            temp = [x + y for x, y in zip(vindict[vin2], dlist)] #Add the current values ontop of whatever is in the dict
            vindict[vin2] = temp
            #print "loop"
        
        else:
            vindict[vin2] = dlist
            #print "loop"

    #Dict isn't printable so loop through the items and print them out
    for keyz in vindict.keys():
        print '%s\t%s' % (keyz, vindict[keyz])
		
if __name__ == "__main__":
    main(sys.stdin)