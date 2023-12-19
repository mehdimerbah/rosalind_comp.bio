#!/usr/bin/env python3 


import sys
import re

try:
    dna_seqs = open("dna_seqs.txt", 'rt')
except:
    print("File Not Found!")
    sys.exit()


main_seq = ''
introns = []
main_flag = 0
for line in dna_seqs:
    if '>' in line and main_flag == 0:
        main_flag = 1
        main_seq = dna_seqs.readline().strip()
    elif '>' in line and main_flag == 1:
        continue
    else:
        introns.append(line.strip())

intron_expressions = []

for intron in introns:
    intron_pattern = rf'\b{intron}\b'
    intron_expressions.append(intron_pattern)

spliced = []

for ptrn in intron_expressions:
    search = re.search(ptrn, main_seq)
    if search is not None:
        for hit in re.finditer(ptrn, main_seq):
            tmp = main_seq[:hit.start()] + main_seq[hit.end()+1:]
            print(tmp)

    else:
        print('No Intron Found')