#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv(sys.argv[1], sep="\t", header=0, index_col=0)
arr = df.to_numpy()

arr2=np.delete(arr, [2,3,4,5],1)

kmean= KMeans(n_clusters=5) #number of clusters you think you have

kmean.fit(arr2)
kmean.cluster_centers_
kmean.labels_

fig,ax=plt.subplots()
plt.scatter(arr2[:,0], arr2[:,1], alpha=0.5,c=kmean.labels_.astype(float))
plt.xlabel("CFU")
plt.ylabel("poly")
ax.set_title("k-means clustering")
fig.savefig("kmean.png")
plt.close(fig)
