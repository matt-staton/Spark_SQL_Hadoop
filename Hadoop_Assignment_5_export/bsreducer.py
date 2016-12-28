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
		print m
		
if __name__ == "__main__":
    main(sys.stdin)