#!/usr/bin/python

import sys
import re
from collections import defaultdict

# --- get all lines from stdin ---
for line in sys.stdin:

    # -- Define an empty default dictionary-----
    def_dict = defaultdict()

    # Strip unwanted characters
    line = line.strip()

    # --- Split the messages by tab to extract To, From , Cc, Bcc references
    elements = line.split('\t')

    # -- Creating a dictionary where keys are references(From,to etc.) and values are the respective email ids
    for i in elements:
        temp = ((i.split(':')))
        if temp[0] in ('Message-ID', 'From', 'To', 'Cc', 'Bcc'):
            def_dict[temp[0]] = re.findall(r'[\w\.-]+@[\w\.-]+', temp[1])

    # --- Creating a dictionary in the Map output format with key as reference,email id pair and value as message id
    def_dict_op = defaultdict()
    for i in def_dict.keys():
        if i != 'Message-ID':
            for e in def_dict[i]:
                def_dict_op[i + ':' + e.lower()] = def_dict['Message-ID']

    # --- Printing the final result as lines
    for feature in def_dict_op.keys():
        print '%s\t%s' % (feature, def_dict_op[feature])
