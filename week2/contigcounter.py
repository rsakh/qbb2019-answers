#!/usr/bin/env python3

"""
Parse and print all records from a FASTA file 
"""

import sys

class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False #eof =end of file
        
    def next(self):
        
        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            #If we reach here, odent is set correctly    
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
                
        sequence = "".join(sequences)
        return ident, sequence

#What I want to work:

reader = FASTAReader(open(sys.argv[1]))

number_of_contigs = 0
contig_length = []


while True:
    ident, sequence = reader.next()
    number_of_contigs += 1
    contig_length.append(len(str(sequence)))
    contig_length.sort(reverse = True)
    
    if ident is None:
        break
    
    total = sum(contig_length)
    count = len(contig_length)
    average = total/count  
    n50 = total/2
    
sum_n50=0
count_n50 = 0

for i in contig_length:
    if sum_n50<=n50:
        sum_n50 += i #finding the middle of the whole thing
        count_n50 += 1 #finding middle position

print (number_of_contigs, "number of contigs")
print (average, "average")
print (contig_length[count_n50], "n50")
print (contig_length[0], "min") 
print (contig_length[len(contig_length)-1], "max")


