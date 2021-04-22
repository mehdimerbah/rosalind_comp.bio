#!/usr/bin/python3
import sys



args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()

entries = {}
n = 0

for line in f:
    if '>' in line:
        seq_id = line.strip()[1:]
        entries[seq_id] = []
    else:
        stripped = list(line.strip())
        #curr = list(entries[seq_id])
        entries[seq_id].extend(stripped)

        
n = len(list(entries.values())[0])



bases = {"A" : [],
         "C" : [],
         "G" : [],
         "T" : []}

for itr in range(n):
        bases['A'].append(0) 
        bases['C'].append(0)                 
        bases['G'].append(0)
        bases['T'].append(0)

for itr in range(n):
    for key in entries.keys():
        bases[entries[key][itr]][itr]+=1
        

consensus = []

for itr in range(n):
    max_freq = 0
    max_base = 'A'
    for key in bases.keys():
        if max_freq <= bases[key][itr]:
            max_freq = bases[key][itr]
            max_base = key
    consensus.append(max_base)
    
print("".join(consensus))

for key in bases.keys():
    print("%s:" % key, end="")
    for itr in range (n):
         print(" ", bases[key][itr], end="")
    print()


f.close()
