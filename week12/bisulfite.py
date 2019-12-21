#!/usr/bin/env python3

import sys
file1 = open(sys.argv[1]) #CpG_context_SRR1035452_1_bismark_bt2_pe.txt
file2 = open(sys.argv[2]) #CpG_context_SRR1035454_1_bismark_bt2_pe.txt


everything_file1 = {}
everything_file2 = {}
file1_meth = []
file2_meth = []
same =[]

for i, line in enumerate(file1):
    if i == 0:
        continue
    file1_start = line.rstrip().split()[3]
    methylation = line.rstrip().split()[4]
    if methylation == 'Z':
    #if methylation >= 50:
        everything_file1[file1_start] = 1
    if methylation == 'z':
        everything_file1[file1_start] = 0
   
for i, line in enumerate(file2):
    if i == 0:
        continue
    file2_start = line.rstrip().split()[3]
    methylation = line.rstrip().split()[4]
    if methylation == 'Z':
       everything_file2[file2_start] = 1
    if methylation == 'z':
       everything_file2[file2_start] = 0


for item in everything_file1:
    if item not in everything_file2:
        continue
    if everything_file1[item] == everything_file2[item]:
        same.append(item)

output=open("sameoutput.csv","w")
for i in same:
    output.write(i+"\n")
    
for item in everything_file1:
    if item not in everything_file2:
        continue
    if (everything_file1[item] == 1) and (everything_file2[item]==0):
        file1_meth.append(item)

output2=open("file1methoutput.csv","w")
for i in file1_meth:
    output2.write(i+"\n")

for item in everything_file1:
    if item not in everything_file2:
        continue
    if (everything_file1[item] == 0) and (everything_file2[item]==1):
        file2_meth.append(item)

output3=open("file2methoutput.csv","w")
for i in file2_meth:
    output3.write(i+"\n")
