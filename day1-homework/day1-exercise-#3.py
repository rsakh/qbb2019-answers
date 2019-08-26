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
    #ref each column
    #striping the return so that it just reads the NH:i:1 with out the space afterwards
    fields =line.rstrip("\n").split("\t")
    #break up in to the columns
    for field in fields:
        if field == "NH:i:1":
            count += 1
print(count)


