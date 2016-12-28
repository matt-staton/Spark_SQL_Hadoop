#!/usr/bin/python
import sys

#create empy dictionary
word2count = {}

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # parse input from mapper
    word, msg, count, sos = line.split('\t')

    # convert to string
    try:
        msg = int(msg)
        count = int(count)
        sos = int(sos)
		
    except ValueError:
        continue

    # Create tuple of word, #msgs, count, sos, min, max, mean, variance
	# This is where we sum up stats by word
	# Try statement attempts to add stats to word if it exists in the dictionary
	# Except creates the key for the word if it is not present in the dictionary
    try:
        word2count[word] = [(word2count[word][0] + msg),
							(word2count[word][1] + count),
							(word2count[word][2] + sos),
                            min(count, word2count[word][3]),
							max(count, word2count[word][4])]
    except:
        word2count[word] = [msg, count, sos, count, count]

# write the tuples to stdout
for word in word2count.keys():
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (word, word2count[word][0],
											  word2count[word][1],
											  word2count[word][2],
                                              word2count[word][3],
											  word2count[word][4],
                                              round(float(word2count[word][1]) / float(word2count[word][0]), 2),
                                              round((float(word2count[word][2]) / float(word2count[word][0])) -
                                              ((float(word2count[word][1]) / float(word2count[word][0])) ** 2), 2))