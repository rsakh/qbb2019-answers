#Question 1
(after copying the SRR file)

/Users/cmdb/qbb2019-answers/day2-lunch $ head -n 40000 ~/data/rawdata/SRR072893.fastq > SRR072893.10k.fastq

fastqc SRR072893.10k.fastq 

open SRR072893.10k_fastqc.html

/Users/cmdb/qbb2019-answers/day2-lunch $ hisat2 -p 4 -x ~/qbb2019-answers/genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam

/Users/cmdb/qbb2019-answers/day2-lunch $ samtools sort -@ 4 -O BAM SRR072893.10k.sam > SRR072893.10k.bam

samtools index SRR072893.10k.bam 

stringtie SRR072893.10k.bam -G ~/qbb2019-answers/genomes/BDGP6.Ensembl.81.gtf -o SRR072893.10k.gtf -p 4 -B -e

ls -lR /Users/cmdb/qbb2019-answers/day2-lunch > output

#Question 3
 (so you have to sort the gtf file and feed that into the cut function, where you just want to read the first column with the chromosome names, then you do uniq -c to group them so that you can count them in their corresponding groups/clusters. That is how you can calc how many alignments are on each chromosome)
/Users/cmdb/qbb2019-answers/day2-lunch $ sort SRR072893.10k.gtf | cut -f 1 | uniq -c > lunchnumber3

#question4
lines with 12 columns have bad reads 
lines with 20 or more columns have good reads that map well
