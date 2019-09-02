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
    extender[ident] = sequence #making a dictionary with extended kmers? why do we have this here? we dont mention extended kmers until later?
    for j in range(0, len(sequence) - k +1): # groupings, math problems thing that siran showed me
        kmer = sequence[j:j+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident,j)) #if kmer is there, then you are going to add it into the dictionary, but if not there then what is the else doing?
        else:
            target_dict[kmer]=[(ident,j)]
# print(target_dict)

for ident, sequence in query:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        #print (kmer)
        if kmer in target_dict:
            for ident, j in target_dict[kmer]: #if the kmer is in the target dict then you want to extend it
                target_seq = extender[ident] # I'm reassigning the target sequence dictionary here
                target_length = len(target_seq) #defining a new input for target seq because for statement for query overrides the for statement for target seq?
                query_length = len(sequence) #query seq

                extend_right = True #assigning the variable as True
                extended_kmer = kmer

                while extend_right == True:
                    if sequence[i+k+1] == target_seq[j+k+1]:
                        i += 1
                        j += 1
                        extended_kmer += sequence[i+k+1]

                    elif (j+k == target_length) or (i+k == query_length): #this means that there isn't a matching base next to the kmer? or that it stops?
                        final_dict[extended_kmer].append((ident), i)
                        extend_right = False

                    else:
                        final_dict[extended_kmer].append((ident), i)
                        extend_right = False # could write break instead, right?
                        break
                print(final_dict[extender_kmer])
        #final_dict[extended_kmer].append((ident), i)
                #this is where i would add to my final dict where I would add my extention
                #print (extended_kmer,i)
                # print (ident, i)