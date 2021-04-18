#!/usr/bin/python3
import sys
import re


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

for line in f:
    if '>' in line:
        seq_id = line.strip()[1:]
        entries[seq_id] = ""
    else:
        stripped = line.strip()
        entries[seq_id] = entries[seq_id] +  stripped


min_len = 2000
for key, val in entries.items():
    if(len(val) < min_len):
        min_len = len(val)
        min_key = key

st = 0
end = 1
motif = ""

while(end<=min_len):
    flag = 0
    pattern = entries[min_key][st:end]
    for val in entries.values():
        if re.search(pattern, val) is None :
            st += 1
            end = st+1
            flag = 1
            break
    if flag == 1:
        continue
    
    else:
        if len(pattern)>len(motif):
                motif = pattern
        end += 1
    



print("The Motif is: ", motif)


f.close()
