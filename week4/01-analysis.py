#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

pca1_list = []
pca2_list = []
af_val_list = []
fam = set()
fam_colors={}
fam_tup = []

for line in open(sys.argv[1]): #1stPCA.eigenvec
    x_val = float(line.rstrip().split()[2])
    y_val = float(line.rstrip().split()[3])
    family = line.rstrip().split()[0]
    #pca1_list.append(x_val)
    #pca2_list.append(y_val)
    fam_tup.append((family, x_val, y_val)) 
    fam.add(family) #adding the families into a list... but 
     
fam = list(fam)
#print (fam)
colors = ['#800000', '#9A6324', '#e6194B', '#808000', '#ffe119', '#469990', '#000075', '#000000', '#f032e6', '#aaffc3', '#a9a9a9']
for i in range(len(fam)):
    fam_colors[fam[i]] = colors[i]

    #print (pca1_list)
    #print (pca2_list)
for line in open(sys.argv[2]): #vcf
    if line.startswith("#"):
        continue
    allele_freq = line.rstrip().split()[7]
    af_value = allele_freq.split("=")[1]
    #af_val_list.append(af_value)
    if "," not in allele_freq:
        af_val_list.append(float(af_value))
    elif "," in allele_freq:
        af_val_list.append(float(af_value.split(",")[0]))
    #print(af_val_list)
    #print (af_value)

fig, ax = plt.subplots()
for point in fam_tup:
    ax.scatter (point[1], point[2], color = fam_colors[point[0]])
ax.set_title("Genetic Variance")
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
fig.savefig("Figure1")
plt.close(fig)
              
fig, ax1= plt.subplots()
ax1.hist(af_val_list,bins=1000)
ax1.set_title("Allele Frequency across SNPs")
ax1.set_xlabel("SNPs")
ax1.set_ylabel("Allele Frequency")
fig.savefig("Figure2")
plt.close(fig)