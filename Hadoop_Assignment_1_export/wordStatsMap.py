#!/usr/bin/python
import sys

#--begin tracking line_number or message number--#
line_num = 0

#--- get all lines from stdin ---
for line in sys.stdin:
line_num += 1

    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()

    #--begin tracking the word number --#
    word_num = 0

    #--create dictionary for word counts--#
    dict = {}
    #--- output tuples [word, line_num, word_line_total, sos] in tab-delimited format---
    for word in words:
        # For each word in the line, output a key/value pair
        # with the word as the key, and "1" as the value.

        if word in dict
            dict

        print '%s\t%s' % (word, 1)
