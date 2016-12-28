#!/usr/bin/python

import sys
from collections import defaultdict

# -- Define a dictionary which can hold list-----
new_dict = defaultdict(list)

# -- Split by tab into roll and message id
for line in sys.stdin:
    line = line.strip()
    roll, message = line.split('\t', 1)
    message = message.strip('[').strip(']').strip("'")

    # -- Append message ids if roll already exists
    try:
        # -- Making sure there are no duplicate message ids
        if message not in new_dict[roll]:
            new_dict[roll].append(message)

    # -- If not, create new pair
    except:
        new_dict[roll] = [None]
        new_dict[roll][0] = message

# --- Print the results
for roll in new_dict.keys():
    print '%s\t%s' % str(sorted(new_dict[roll])).strip(  "[']").replace("', '", ", ")
