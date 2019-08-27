#!/usr/bin/env python3

import sys

gene_id = {} #make dictionary to correlate the uniprot ids to the gene/flybase ids
      
for line in open(sys.argv[1]):
    column = line.rstrip("\n").split("\t")
    uniprot_id = column[1].rstrip()
    flybase_id = column[0].rstrip()
    gene_id[flybase_id] = uniprot_id
    
for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
          
    columns = line.rstrip("\n").split("\t")
    flybase_id = columns[8] #got this from ../results/stringtie/SRR072893/t_data.ctab so we can compare uniprot ids to these gene ids
    
    #if they match, then it will print the uniprot id and other stuff
    if flybase_id in gene_id:
        uniprot_id = gene_id[flybase_id]
        print(line.rstrip("\n"), uniprot_id)
    else:
        if "-x" in sys.argv[2]:  
            print(line.rstrip("\n"), '*') #will print * if no matching uniprot id
        else:
            pass
        
        
        
       



    
