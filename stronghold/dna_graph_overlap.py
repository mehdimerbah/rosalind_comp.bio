#!/usr/bin/python3
import sys


try:
    f = open("rosalind_grph.txt", 'rt')
except:
    print("File Not Found!")
    sys.exit()

reads_dict = {}

for line in f:
    if '>' in line:
        seq = ''
        seq_id = line.strip()[1:]
    else:
        seq += line.strip()
        reads_dict[seq_id] = seq


adj_list = []

for seq_1_id, seq_1 in reads_dict.items():
    for seq_2_id, seq_2 in reads_dict.items():
        if seq_1 == seq_2:
            continue;
        else:
            if seq_1[len(seq_1)-3:] == seq_2[0:3]:
                adj_list.append([seq_1_id, seq_2_id]) 


answer_file = open('overlap_graphs.txt', 'wt')

for pair in adj_list:
    answer_file.write(f'{pair[0]} {pair[1]}\n')

answer_file.close()
f.close()

    


	
