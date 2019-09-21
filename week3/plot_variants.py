#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

dp_list = []
qs_list = []
af_list = []
ann_dict = {}

for line in open(sys.argv[1]): #snpeff
    if line.startswith("#"):
        continue
    fields = line.rstrip("\t").split()
    chrom = fields[0]
    pos = fields[1]
    ref_base = fields[3]
    alt_base = fields[4]
    qual_score = int(float(fields[5]))
    
    info = fields[7]
        
    dp_split=info.split(";")[7]
    dp = dp_split.split("=")[1]
    dp_list.append(dp)

    qs_list.append(qual_score)

    af_split = info.split(";")[3]
    af_list.append(af_split.split("=")[1])

    ann_split = info.split(";")[41]
    ann_value = ann_split.split("=")[1]
    ann_score = ann_value.split("|")[1]
    
#print (ann_score_list)
    if ann_score in ann_dict:
        ann_dict[ann_score] += 1
    else:
        ann_dict[ann_score] = 1

#print (ann_dict)
#print (af_list)
#print(qs_list)
#print (type(dp))

#print(dp_list)
#print (dp)
    
#FIG #1
# fig, ax = plt.subplots()
# ax.hist(dp_list, bins=100)
# fig.savefig( "test" )
# plt.close(fig)

#FIG #2
# fig, ax = plt.subplots()
# ax.hist(qs_list, bins=1000, range=[0, 5000])
# fig.savefig( "test2" )
# plt.close(fig)

#FIG #3
# fig, ax = plt.subplots()
# ax.hist(af_list, bins=100, range = [0, 50000])
# fig.savefig( "test3" )
# plt.close(fig)

# #FIG #4
# plt.bar(range(len(ann_dict)), list(ann_dict.values()), align = 'center')
# plt.xticks(range(len(ann_dict)), list(ann_dict.keys()))
# plt.show()

fig,ax = plt.subplots(4)

ax[0].hist( dp_list, bins=100)
ax[1].hist( qs_list, bins=1000, range=[0, 5000])
ax[2].hist( af_list, bins=100)
plt.bar(range(len(ann_dict)), list(ann_dict.values()), align = 'center')
plt.xticks(range(len(ann_dict)), list(ann_dict.keys()), rotation = 'vertical', size = 5)

ax[0].set_xlabel("Variants")
ax[0].set_ylabel("Read Depth")

ax[1].set_xlabel("Variants")
ax[1].set_ylabel("Quality")

ax[2].set_xlabel("Variants")
ax[2].set_ylabel("Frequency")

ax[3].set_xlabel("Variants")
ax[3].set_ylabel("Impact")

ax[0].set_title("Read Depth Graph")
ax[1].set_title("Quality Graph")
ax[2].set_title("Allele Frequency Graph")
ax[3].set_title("Impact Graph")


fig.savefig( "results.png" )
plt.close(fig)

    
        