#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

sequence=open(sys.argv[2])
peaks=open(sys.argv[1])
output_file=open(sys.argv[3], 'w')
sequence_index=""
position={}
for i,line in enumerate(peaks):
   field=line.rstrip("\n").split()
   position[field[3]]=[field[1],field[2]]
#print(position)
#    position[]
#quit()
for i in sequence:
   if i.startswith(">"):
       continue
   field2=i.rstrip("\n")
   sequence_index+=str(field2)
#print(sequencetotal)
#quit()
sequencesident=[]
count=0
for key,value in position.items():
   #print(key)
   count+=1
   output_file.write('>{}\n{}\n'.format(count,(sequence_index[int(value[0]):int(value[1])])))
output_file.close()





