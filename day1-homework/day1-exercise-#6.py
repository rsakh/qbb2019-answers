#!/usr/bin/env python3

#count number of alignments

import sys

#argument you put right after $. and 1 refers to second argument
if len(sys.argv)>1:
    f = open(sys.argv[1])
    
else:
    f = sys.stdin
    
count = 0

for line in f:
    # filter lines that begin with @
    if line.startswith("@"):
        continue
    #ref each column
    fields =line.split("\t")
    if fields[2] == "*":
        continue 
    if int(fields[3]) >= 10000:
        if int(fields[3]) <= 20000:
            if fields[2] == "2L":
                count+= 1
print(count)


