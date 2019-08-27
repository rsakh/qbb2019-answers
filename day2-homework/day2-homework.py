#!/usr/bin/env python3

import sys

for line in (sys.stdin):
    #filter so that you only get DROME and that the last column contains fbgn because some of the lines in the 4th column are empty
    if "DROME" and "FBgn" not in line:
        continue
    #eliminate the whitespace and returns   
    fields = line.rstrip("\n").split()
    #count the columns backwords because the first two columns are not always filled in so it may assume that it has one less column    
    uniprot = fields[-2]
    flybase = fields[-1]
    
    print(flybase, "\t", uniprot)
        
