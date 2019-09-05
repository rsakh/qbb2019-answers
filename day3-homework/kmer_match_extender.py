#!/usr/bin/env python3

#help from TA Kate, Amanda, and Raquel
#this was mad hard, yo

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
            target_dict[kmer].append((ident,j)) 
        else:
            target_dict[kmer]=[(ident,j)]
# print(target_dict)
i = 0
j = 0
for ident, sequence in query:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k +1):
        kmer = sequence[i:i+k]
        #print (kmer)
        if kmer in target_dict:
            for ident, j in target_dict[kmer]: #if the kmer is in the target dict then you want to extend it
                target_seq = extender[ident] # I'm reassigning the target sequence dictionary here
                target_length = len(target_seq) 
                query_length = len(sequence) #query seq

                extend_right = True #assigning the variable as True
                extended_kmer = kmer
                

                while extend_right == True:
                    if (j+k == target_length) or (i+k == query_length): #when we reach the end
                        if ident in final_dict:
                            final_dict[ident].append(extended_kmer) 
                        else:
                            final_dict[ident]=[(extended_kmer)] 
                        break
                        
                    if sequence[i+k] == target_seq[j+k]:
                        i += 1
                        j += 1
                        extended_kmer += sequence[i+k]

                    else:
                        if ident in final_dict:
                            final_dict[ident].append(extended_kmer)
                        else:
                            final_dict[ident]=[(extended_kmer)] 
                        break
                        
#turn all the values of the dictionary into a list   
final_list= []
for kmers in final_dict.values():
   for seqs in kmers:
       final_list.append(seqs)

for kmer in sorted(final_list, key=len, reverse=True):
   print (kmer, len(kmer))