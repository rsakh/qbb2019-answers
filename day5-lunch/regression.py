#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import scipy
import statsmodels.api as sm

df = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name") #making columns... before was object and we have to make it so that we can read it
fpkm = pd.DataFrame(df.loc[:,"FPKM"]) #separated out the FPKM column so its the only column but it is indexed by the t_name

col_names = df.columns.values.tolist()

#print(fpkm)

# #now i just want the "mean"/last column of the histone tab files.
H3K4me1df = pd.read_csv(sys.argv[2], sep = "\t", names = ["t_name", "size", "covered", "sum", "mean0", "mean_x"], index_col = "t_name") #since file doesnt have column names adding them on, so that refer to "t_name" for the stuff i want to do

#parse out mean columns
H3K4me1 = pd.DataFrame(H3K4me1df.loc[:,["mean_x"]])

#print(H3K4me1)
H3K4me3df = pd.read_csv(sys.argv[3], sep = "\t", names = ["t_name", "size", "covered", "sum", "mean0", "mean_y"], index_col = "t_name")
H3K4me3 = pd.DataFrame(H3K4me3df.loc[:,["mean_y"]])
#print(H3K4me3)

H3K9me3df = pd.read_csv(sys.argv[4], sep = "\t", names = ["t_name", "size", "covered", "sum", "mean0", "mean_z"], index_col = "t_name")
H3K9me3 = pd.DataFrame(H3K9me3df.loc[:,["mean_z"]])
#print(H3K9me3)

# #okay, so i have to merge these data frames so they are indexed by the same t_name

df_merge = pd.merge(pd.merge(pd.merge(fpkm,H3K4me1, on="t_name"), H3K4me3, on="t_name"), H3K9me3, on="t_name")
#omg it worked!!
#print (df_merge)


model = sm.formula.ols(formula = "FPKM ~ mean_x + mean_y + mean_z", data=df_merge) #~ means depends on
ols_result = model.fit () #least squares fitting
print (ols_result.summary()) 

