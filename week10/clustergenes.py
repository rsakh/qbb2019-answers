#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pandas as pd
import seaborn as sb
import scipy.cluster.hierarchy as hac

from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram

df = pd.read_csv(sys.argv[1], sep="\t", header=0, index_col=0)
arr = df.to_numpy()

Z = hac.linkage(arr,"average")
sorted_Z = hac.leaves_list(Z)

sorted_arr = []
for i in sorted_Z:
    sorted_arr.append(arr[i])
sorted_arr = np.array(sorted_arr) #clustered based on gene

trans_arr = sorted_arr.transpose()

Z = hac.linkage(trans_arr, 'average')
sorted_Z = hac.leaves_list(Z)
print(sorted_Z)

double_sorted_arr = []
for i in sorted_Z:
    double_sorted_arr.append(trans_arr[i])
double_sorted_arr = np.array(double_sorted_arr)

trans_back = double_sorted_arr.transpose()

columns = df.columns

x = []
for i in sorted(sorted_Z):
    x.append(columns[i])
    
x1 = []
for i in sorted_Z:
    x1.append(columns[i])
    

fig,(ax1,ax2,ax3) = plt.subplots(ncols=3, figsize=(12,8))

sb.heatmap(arr, ax=ax1)
sb.heatmap(sorted_arr, ax=ax2)
sb.heatmap(trans_back, ax=ax3)

ax1.set_ylabel("genes")
ax1.set_xlabel("cell type")
ax1.set_title("unsorted cluster")
ax1.set_xticklabels(x)
ax1.set_yticks([])

ax2.set_ylabel("genes")
ax2.set_xlabel("cell type")
ax2.set_title("cluster based on gene")
ax2.set_xticklabels(x)
ax2.set_yticks([])

ax3.set_ylabel("genes")
ax3.set_xlabel("cell type")
ax3.set_title("cluster based on gene and cell type")
ax3.set_xticklabels(x1)
ax3.set_yticks([])

plt.tight_layout()
fig.savefig("heatplots.png")
plt.close(fig)

fig,ax = plt.subplots()
hac.dendrogram(Z, labels=x1)
# ax.set_xticklabels(x1)
fig.savefig("dendrogram.png")
plt.close(fig)

