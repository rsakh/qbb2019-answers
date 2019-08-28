#!/usr/bin/env python3

import sys

gene_list = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    fields = line.rstrip("\n").split()
    if ('gene_biotype "protein_coding"' not in line) or ("3R" not in line) or (fields[2] != "gene"):
        continue
    
    gene_start = fields[3]
    gene_end = fields[4]
    gene_id = fields[13]
    gene_list.append((int(gene_start), int(gene_end), gene_id))
    

gene_list.sort()
#made my list!!

search_pos = 21378950
search_chrom = "3R"

lo = 0
hi = len(gene_list)-1
mid = 0
number_iterations = 0

while (lo < hi):
    mid = int((hi+lo) /2)
    number_iterations += 1
    if search_pos < gene_list [mid][0]:
        hi = mid 
    elif search_pos > gene_list [mid][1]:
        lo = mid + 1
    else:
        break
            
print(gene_list[lo], number_iterations)
            
        