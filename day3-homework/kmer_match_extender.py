#!/usr/bin/env python3

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) #subset.fa
query = FASTAReader(open(sys.argv[2])) #droYak2_seq.fa
k = int(sys.argv[3])

target_dict = {}
extender = {}
final_dict = {}

for ident, sequence in target:
    sequence = sequence.upper()
    extender[ident] = sequence
    for j in range(0, len(sequence) - k +1):
        kmer = sequence[j:j+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident,j))
        else:
            target_dict[kmer]=[(ident,j)]
            
   # print(target_dict)

for ident, sequence in query:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            for ident, j in target_dict[kmer]:
                target_seq = extender[ident]
                target_length = len(target_seq)
                query_length = len(sequence) #query seq
                extend_right = True
                extended_kmer = kmer
                while True:
                    if extend_right:
                        if sequence[i+k+1] == target_seq[j+k+1]:
                            i += 1
                            j += 1
                            extender_kmer += sequence[i+k+1]
                        else:
                        extend_right = False
                    else:
                        #this is where i would add to my final dict where I would add my extention
                        break
                    if (j+k == target_length) or (i+k == query_length):
                        extend_right = False
                
                        




