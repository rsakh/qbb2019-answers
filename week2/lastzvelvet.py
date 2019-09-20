#!/usr/bin/env python3
import sys

import matplotlib.pyplot as plt

target_start_sites = []   
contig_start_sites = []

target_end_sites = []   
contig_end_sites = []

list_ = []
contig_dict = {}

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    fields = line.rstrip("\n").split()
    # no_mismatch= line.split()[0]
    if fields[6] == "+":
        ref_start= int(fields[3])
        ref_end = int(fields[4])
        contig_start = int(fields [7])
        contig_end = int(fields[8])
        contig_length = abs(contig_end - contig_start)

        contig_dict[int(ref_start)]=[ref_start, ref_end, contig_length]
# for key in sorted(contig_dict):
#     print (key)
ref_start_list = []
ref_end_list =[]
contig_length_list = []
for key in sorted(contig_dict):
    ref_start_list.append(contig_dict[key][0])
    ref_end_list.append(contig_dict[key][1])
    contig_length_list.append(contig_dict[key][2])

#print(ref_start_list, ref_end_list, contig_length_list)
    

fig, ax = plt.subplots()
count = 0
for i in range(len(ref_start_list)):
    plt.plot([count, count+contig_length_list[i]], [ref_start_list[i], ref_end_list[i]], "r-") #leng og ref is y, total len of contigs =x
    count += int(contig_length_list[i])
    
ax.set_title("Assembly Plot 5")
ax.set_xlabel("Contigs")
ax.set_ylabel("Reference Genome")
# plt.ylim((20000,100000))
# plt.xlim((0,4000))
plt.tight_layout()
fig.savefig("BetterCoverageVelveth.png")
plt.close()


        
        
       
      