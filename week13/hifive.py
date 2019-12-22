#!/usr/bin/env python2
import sys
import hifive
import numpy

rna = open(sys.argv[1])
activity= open(sys.argv[2])

hic = hifive.HiC('PROJECT_FNAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

rna_dict = {}
activity_dict = {}

for i, line in enumerate(rna):
    if i==0:
        continue
    start = int(line.rstrip().split()[1])
    rna_exp = float(line.rstrip().split()[4])
    ########## need dylan to explain this to me again!!!
    if (start >= 5000000) and (start <40000000):
        rel_start = (start - 5000000)/5000
        rna_dict[rel_start]=rna_exp
        
for i, line in enumerate(activity):
    if i==0:
        continue
    start = int(line.rstrip().split()[1])
    enh_act = float(line.rstrip().split()[4])
    if (start >= 5000000) and (start <40000000):
        rel_start = (start - 5000000)/5000
        activity_dict[rel_start]=enh_act
        
### yeah, son.. imma take the L on this because I need Dylan to explain this to me again for the 3rd time. I have problems. But you know what? Life still rips. You should know that I really did try to finish all the assignments to the best of my ability. I know the point of this assignment is to correlate the predicted expression of the genes using combined/ additive enhancer activity to actual gene expression (via RNA seq data).