#!/usr/bin/env python3
## this is for ploting the motifs within the binding sites

import sys
import matplotlib.pyplot as plt
import seaborn as sb

fimo = open(sys.argv[1]) #motifs
binding_site = open(sys.argv[2]) #ER4sorted.bed #binding sites

fimo_start_dict= {}

for line in fimo:
    if line.startswith("#"):
        continue
    binding_site_sample = int(line.rstrip("/n").split()[0])
    strand = line.rstrip("\n").split()[6]
    #print (strand)
    fimo_start = int(line.split()[3])
    fimo_end = int(line.split()[4]) -1#minus for offset
    #print(strand, fimo_start, fimo_end)

    if strand == "+" in line:
        fimo_start= fimo_start

    if strand == "-" in line:
        fimo_start = fimo_end
    
    fimo_start_dict.setdefault(binding_site_sample, [])
    fimo_start_dict[binding_site_sample].append(fimo_start)
    
#print(fimo_start_dict)

locations= []
    #print (fimo_start)
for i,line in enumerate(binding_site, 1):
    sample = i
    binding_start = int(line.split()[1])
    binding_stop = int(line.split()[2])
    length = binding_stop - binding_start
    for motif_start in fimo_start_dict[sample]:
        rel_loc = motif_start/length
        locations.append(rel_loc)
        
fig, ax = plt.subplots()
sb.distplot(locations,bins=20, ax=ax)

ax.set_xlabel("Relative location of motif within binding site")
ax.set_ylabel("amount")
ax.set_title("Histogram")
fig.savefig("hist.png")
plt.close(fig)
#print(locations)
    #print (length)
    
