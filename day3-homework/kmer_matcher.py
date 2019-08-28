#!/usr/bin/env python3

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) #subset.fa
query = FASTAReader(open(sys.argv[2])) #droYak2_seq.fa
k = int(sys.argv[3])

target_dict = {}

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident,i))
        else:
            target_dict[kmer]=[(ident,i)]
            
   # print(target_dict)

for ident, sequence in query:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            for ident, j in target_dict[kmer]:
                print(ident, j, i, kmer)
    
    

