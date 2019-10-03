#!/usr/bin/env python
#If you have several versions of Python installed, /usr/bin/env will ensure the interpreter used is the first one on your environment's $PATH


import sys

#input comes from STDIN (standard input)
for line in sys.stdin:
        #remove leading and trailing whitespace
        line = line.strip()
        #split the line into words
        words = line.split()

        #update counters
        for word in words:
                #write the results to STDOUT
                #what we output here will be the input for the reduce step
                #i.e. the input for reducer.py
                print '%s\t%s' % (word,1)
