#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], sep="\t")

goi_p = df.loc[:, "strand"] == "+"
goi_n = df.loc[:,"strand"] == "-"

p_start = df.loc[goi_p, ["chr", "start", "end", "strand", "t_name"]]
n_end = df.loc[goi_n, ["chr", "start", "end", "strand", "t_name"]]

#print(p_start, n_end)

p_start.loc[:, "start"] -= 500
p_start.loc[:,"end"] = p_start.loc[:,"start"] + 1000

n_end.loc[:,"end"] += 500
n_end.loc[:,"start"] = n_end.loc[:,"end"] - 1000

#print(p_start, n_end)
#p_start.loc[p_start.loc[:, "start"] <= 0, 'start'] = 1

roi = p_start.loc[:, "start"] <= 0 #looking for the rows with less than 0
p_start.loc[roi, "start"] = 1

roi2 = n_end.loc[:, "start"] <=0
n_end.loc[roi2, "start"] = 1

new_df = p_start.append(n_end)

new_df = new_df.drop(columns="strand")
#print(new_df)

new_df.to_csv("promoter.bed", sep="\t", header=None, index=False)
