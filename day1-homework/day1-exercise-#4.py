#!/usr/bin/env python3

#count number of alignments

import sys

#argument you put right after $. and 1 refers to second argument
if len(sys.argv)>1:
    f = open(sys.argv[1])
    
else:
    f = sys.stdin

chromosome = []
for line in f:
    # filter lines that begin with @
    if line.startswith("@"):
        continue
    #ref each column
    fields =line.split("\t")
    if fields[2] == "*":
        continue 
    chromosome.append(fields[2])
    if len(chromosome) >= 10:
        break
print(chromosome)


