#!/usr/bin/env python3

import sys
import pandas as pd
from scipy import stats
import scipy.stats as sp
from sklearn.cluster import KMeans

df = pd.read_csv(sys.argv[1], sep='\t', header=0, index_col=0)
diff_exp_high = ((df['CFU'] + df['unk'])/2)/((df['poly'] + df['int'])/2) >= 2
diff_exp_low = ((df['CFU'] + df['unk'])/2)/((df['poly'] + df['int'])/2) <= 0.5
diff_exp_genes = df[diff_exp_high | diff_exp_low]

#print(diff_exp_genes)

#output=open("sigpval.txt", 'w')
for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    # print(gene_name, stats.ttest_rel(sample1, sample2).pvalue)
    pval = stats.ttest_rel(sample1, sample2).pvalue
    if pval <= 0.05:
        print(gene_name, pval)
        #output.write(str(pval))
#output.close()


rel_data = df[['CFU','poly']]
kmeans = KMeans(n_clusters=5).fit(rel_data)
labels = list(kmeans.labels_)
genes = list(rel_data.index.values)
goi_index = genes.index(sys.argv[2]) #Adcy6
goi_cluster = labels[goi_index]
related_genes = []
for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)
  
print(related_genes)
# with open('list_of_genes.txt', 'w') as f:
#    for item in related_genes:
#        f.write("%s," % item)