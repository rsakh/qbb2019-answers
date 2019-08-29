#!/usr/bin/env python3

"""
Usage: ./02-boxplot.py <gene_name> <sexandstage.csv>

Boxplot all transcripts for a given gene in a given sex
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name") #first column is not a column its key names
# print(df)

goi = df.loc[:,"gene_name"] == gene_name #got 25 trues, 3000 something falses

fpkms= df.drop(columns="gene_name") #drops column named gene name

col_names = fpkms.columns


female_names=[]
for i in col_names:
   if "female" in i:
       female_names.append(True)
   else:
       female_names.append(False)

male_names=[]
for i in col_names:
   if "female" not in i:
       male_names.append(True)
   else:
       male_names.append(False)

#print(female_names)
#print(male_names)

fig, (ax1, ax2) =plt.subplots(nrows=2)
ax1.boxplot(fpkms.loc[goi, female_names].T) 
ax2.boxplot(fpkms.loc[goi, male_names].T)
ax1.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xlabel("Stages of Development")
ax1.set_ylabel("FPKMs")
ax2.set_ylabel("FPKMs")
ax1.set_title("females")
ax2.set_title("males")
fig.suptitle("FPKMs by sex during development")
plt.tight_layout()
plt.subplots_adjust(top=0.9)
fig.savefig("boxplothw2.png")
plt.close(fig)