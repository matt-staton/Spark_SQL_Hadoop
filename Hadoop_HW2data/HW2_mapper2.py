#!/usr/bin/python
import sys

# --- get all lines from stdin ---
for line in sys.stdin:

    # --- remove leading and trailing whitespace---
    line = line.strip()

    # --- convert to lower case
    line = line.lower()

    # --- split the line into words ---
    words = line.split()

    # create a set of words
    uniquewords = set(words)

    # print the word, 1, count of word in line, sum of squares
    for word in uniquewords:
		
		#%s formats to str, \t means seperate with tab
        print '%s\t%s\t%s\t%s' % (word, str(1), words.count(word), words.count(word) ** 2)   