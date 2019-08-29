#!/usr/bin/env python3

"""
Usage: .01-hist.py <ctab>

Plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats



fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue #skips header
    fields = line.rstrip("\n").split("\t") #split each line and strip the white space
    if float(fields[-1]) > 0:
        fpkms.append (float(fields[-1]))  
        
print (len(fpkms))

my_data= np.log2(fpkms)

mu= (float(sys.argv[2])) #5.9
sigma= (float(sys.argv[3]))#2.65
a= (float(sys.argv[4])) #-1.9

x= np.linspace(-15, 15, 100) #100 polints -15 to 15 scale
y1= stats.skewnorm.pdf (x, a, mu, sigma) #what is mu and sigma? mu=mean sigma=stdev
#print(y)
#print (type(y))
y2= stats.norm.pdf (x,mu, sigma) #what is mu and sigma? mu=mean sigma=stdev

#mu=0
#sigma=1

fig, ax = plt.subplots() #fig=the entire image, ax=subpanel, so plot two graphs in one image
ax.hist(my_data, bins=100, density=True) #default bins=10
ax.plot (x,y1, label="skew distribution") 
ax.plot(x,y2, label="normal")
ax.legend()
plt.title("FPKMS in SRR072893 data")
plt.text(-15, 0.15, " mu=%0.2f, sigma=%0.2f, a=%0.2f" %(mu, sigma, a))
plt.xlabel("log2(fpkm)")
plt.ylabel("frequency")
fig.savefig("fpkms1.png")
plt.close(fig)