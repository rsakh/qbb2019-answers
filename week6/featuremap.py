#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

differential_binding_G1E = open (sys.argv[1])
differential_binding_ER4 = open (sys.argv[2])
feature_ER4 = open (sys.argv[3])
feature_G1E = open (sys.argv[4])

loss_counter= 0
for i, line in enumerate (differential_binding_G1E):
    loss_counter += 1
#print (loss_counter)
    
gain_counter = 0
for i, line in enumerate (differential_binding_ER4):
    gain_counter += 1
print(gain_counter)
    
ERprom_count= 0  
ERexon_count = 0
ERintron_count = 0  
ERfeature_plot=[]

for i, line in enumerate (feature_ER4):
    feat1 = line.rstrip().split()[3]
    if feat1 == "promoter":
        ERprom_count += 1
    if feat1 == "exon":
        ERexon_count += 1
    if feat1 == "intron":
        ERintron_count += 1
ERfeature_plot.append(ERprom_count)
ERfeature_plot.append(ERexon_count)
ERfeature_plot.append(ERintron_count)

G1Eprom_count= 0  
G1Eexon_count = 0
G1Eintron_count = 0  
G1Efeature_plot=[]
for i, line in enumerate (feature_G1E):
    feat2 = line.rstrip().split()[3]
    if feat2 == "promoter":
        G1Eprom_count += 1
    if feat2 == "exon":
        G1Eexon_count += 1
    if feat2 == "intron":
        G1Eintron_count += 1
G1Efeature_plot.append(G1Eprom_count)
G1Efeature_plot.append(G1Eexon_count)
G1Efeature_plot.append(G1Eintron_count)

#print (ERfeature_plot, G1Efeature_plot)
x1= ["loss", "gain"]    
fig, (ax1, ax2) = plt.subplots(ncols=2)
ax2.bar(x1[0], loss_counter)
ax2.bar(x1[1], gain_counter)
ax2.set_ylabel("number of sites")
ax2.set_title("CTCF binding after differentiation")


width = 0.35
x2 = ["promoter", "exon", "intron"]
x = np.arange(len(x2))
ax1.bar(x - width/2, G1Efeature_plot, width, label="G1E")
ax1.bar(x + width/2, ERfeature_plot, width, label="ER")
ax1.set_ylabel("number of sites")
ax1.set_xticks(x)
ax1.set_xticklabels(x2)
ax1.set_title("Region of CTCF binding")
ax1.legend()
fig.tight_layout()

fig.savefig( "Plot.png" )
plt.close(fig)

