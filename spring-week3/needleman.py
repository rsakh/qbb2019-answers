#!/usr/bin/env python3

import sys
import numpy as np

# HoxD70 matrix of Chiaromonte, Yap, Miller 2002,
#              A     C     G     T
sigma = [ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ]
index = {'A':0,'C':1,'G': 2,'T':3}
gap = 300

seq1 = "CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"
seq2 = "GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG" 
n=len(seq1) #n=len(s1)+1
m=len(seq2) #m=len(s2)+1

#print(n,m)
score_matrix= np.zeros((n+1,m+1))
traceback_matrix =np.zeros((n+1,m+1))

for i in range(n+1):
    score_matrix[i][0] = -gap * i

#print(i)
for j in range(m+1):
    score_matrix[0][j] = -gap * j
    

#print(j)
#print(traceback_matrix)


for i in range(1,n+1):
    for j in range(1,m+1):
        all_list = []
        
        hor = score_matrix[i][j-1] - gap
        ver = score_matrix[i-1][j] - gap
        dia = score_matrix[i-1][j-1] + sigma[index[seq1[i-1]]][index[seq2[j-1]]]
        all_list.append(hor)
        all_list.append(ver)
        all_list.append(dia)
#print(hor, ver, dia)
#print(all_list)
        score_matrix[i,j]= max(all_list)
        #print(all_list)
        traceback_matrix[i,j]=all_list.index(max(all_list))
#print(traceback_matrix)
#print(score_matrix)

i2=len(seq1)
j2=len(seq2)
seq1_alignment=""
seq2_alignment=""
# while traceback[i2, j2] == 2:
while i2 != 0 and j2 != 0:
    t = traceback_matrix[i2,j2]
    if t == 0: #horizontal
         seq1_alignment+="-"
         seq2_alignment+=str(seq1[i2-1])
         j2 = j2 - 1
    elif t==1: #vertical
        seq1_alignment+=str(seq2[j2-1])
        seq2_alignment+="-"
        i2 = i2 - 1
    elif t==2: #diagonal
        seq1_alignment+=str(seq1[i2-1])
        seq2_alignment+=str(seq2[j2-1])
        i2 = i2 - 1
        j2 = j2 - 1

print(seq1_alignment[::-1])
print(seq2_alignment[::-1])
print(score_matrix[len(seq1),len(seq2)])