#!/usr/bin/env python3

import sys
import scanpy as sc
import matplotlib.pyplot as plt

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")

adata.var_names_make_unique()
#### STEP 1:
# sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
#sc.pl.pca(adata)

# sc.pp.filter_genes(adata, min_counts = 1) #only genes with more than one count
# sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell
#
# filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)
#
# adata = adata[:, filter_result.gene_subset]
# sc.pp.normalize_per_cell(adata)
# sc.pp.log1p(adata)
# sc.pp.scale(adata)
# sc.tl.pca(adata,n_comps=50)
#sc.pl.pca(adata)

#### STEP 2:
## Bruh, Dylan helped me figure out how to make this stuff easier. Because something above was making the terminal freak out
# sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
# sc.tl.pca(adata)
#
# sc.pp.neighbors(adata)
# sc.tl.louvain(adata, resolution=0.3)
#
# fig, ax = plt.subplots()
#
# # sc.tl.tsne(adata)
# # sc.pl.tsne(adata, color=['louvain'], ax=ax, show=False)
#
# sc.tl.umap(adata)
# sc.pl.umap(adata, color=['louvain'], ax=ax, show=False)
#
# plt.show()


#### STEP 3:
## definitely googled this shizzzz
sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.louvain(adata, resolution=0.3)

# fig, ax = plt.subplots()
#
# sc.tl.rank_genes_groups(adata, groupby='louvain', method='t-test')
# sc.pl.rank_genes_groups(adata, groupby='louvain', method='t-test', show=False)
#
# plt.show()

# fig, ax = plt.subplots()
#
# sc.tl.rank_genes_groups(adata, groupby='louvain', method='logreg')
# sc.pl.rank_genes_groups(adata, groupby='louvain', method='logreg', show=False)
#
# plt.show()

#### STEP 4:

