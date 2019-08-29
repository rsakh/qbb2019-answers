#!/usr/bin/env python3

"""
Usage: ./day4_lunchex2.py <ctab1> <ctab2> 

Plot FPKM from two sources
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd


name1=sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep = "\t", index_col="t_name")

name2=sys.argv[2].split(os.sep)[-2] 
ctab2 =pd.read_csv(sys.argv[2], sep = "\t", index_col="t_name")

fpkm = {name1: ctab1.loc[:,"FPKM"],
        name2: ctab2.loc[:,"FPKM"]}
        
df= pd.DataFrame(fpkm)

g_ctab1 = df.loc[:,"SRR072893"]  
g_ctab2 = df.loc[:,"SRR072894"] 

x = np.log2(g_ctab1 +1)
y = np.log2(g_ctab2 +1)

fig, ax = plt.subplots()
ax.scatter( x= x, y= y, s=5, alpha=.15)

plt.title("FPKMS of SRR072893 and SRR072894")
plt.xlabel("log2(FPKM) of SRR072893")
plt.ylabel("log2(FPKM) of SRR072894")

line = np.polyfit(x, y, 1)
xl = np.linspace(0, 10, 10)
yl = line [0]*xl + line[1]
ax.plot(xl, yl, label= "curve", color= "red")
ax.legend()

print(line)
print(type(line))

fig.savefig("scatter.png")
plt.close(fig)

