#!/usr/bin/env python3

#count number of alignments

import sys

#argument you put right after $. and 1 refers to second argument
if len(sys.argv)>1:
    f = open(sys.argv[1])
    
else:
    f = sys.stdin

for line in f:
    # filter lines that begin with @
    if line.startswith("@"):
        continue
    #ref each column
    fields =line.split("\t")
    if fields[2] == "*":
        continue 

with open("SRR072893.SAM") as f:
    total = 0
    count = 0
    for line in f:
        field = line.split("\t")
        if field[2] == "*":
            continue
        total += int(field[4])
        count += 1
result = total / count
print(result)
