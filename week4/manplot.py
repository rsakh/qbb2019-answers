#!/usr/bin/env python3
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

chrom_tup=[]


# chrom_names= []

chrom_colors ={}

for file_name in os.listdir(os.getcwd()):
    if file_name.endswith(".qassoc"):
        position_dict ={}
        print(file_name)
        q_assoc_file = open(file_name)
        for i, line in enumerate(q_assoc_file):
            if i == 0:
                continue
            if "NA" in line:
                continue
            
            p_value = float(line.rstrip().split()[-1])
            chrom = line.rstrip().split()[0]
            
            position = int(line.rstrip().split()[2])

            #chrom_tup.append((chrom, -np.log10(p_value)))
            
            position_dict.setdefault(chrom,[])
            position_dict[chrom].append((position, -np.log10(p_value)))
            
            #chrom_set.add(chrom)
            # if chrom not in chrom_names:
 #                chrom_names.append(chrom)

        for chrom in position_dict:
            position_dict[chrom].sort(key=lambda tup: tup[0])
            #print(position_dict[chrom])
        
        colors = ['#000000', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#a9a9a9']
        color_count = 0
        for chrom in position_dict:
            chrom_colors[chrom] = colors[color_count]
            color_count += 1

        start_point = 1
        fig, ax = plt.subplots()
        for chrom in position_dict:
            points = [position_dict[chrom][i][1] for i in range(len(position_dict[chrom]))]
            colors = ['red' if pval > 5 else chrom_colors[chrom] for pval in points]
            ax.scatter([x for x in range(start_point,start_point+len(points))], points, color = colors, s=2)
            start_point += len(points)
           # for point in chrom_tup:
#                if point[0] == chr:
#                    ax.scatter(start_point, point[1], color = chrom_colors[point[0]], s=2)
#                    if point[1] > 5:
#                        ax.scatter(start_point, point[1], color = "red", s=2)
#                    start_point +=
        #print("i")
        ax.set_xlabel("Chromosome")
        ax.set_ylabel("Frequency")
        ax.set_title(file_name)
        fig.savefig(file_name +'.png')
        plt.tight_layout()
        plt.close(fig)
    


    