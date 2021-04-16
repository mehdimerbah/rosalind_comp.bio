#!/usr/bin/python3
import sys
import re
 ## Given a sequence of DNA ACGTCCCTAAGAGAGT and a motif of length <= len(sequence) find all positions this motif occurs in the sequence



args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()


seq = f.readline().strip()
motif = f.readline().strip()

print(seq, motif)
#print(x)
matches = []
for i in range (0, len(seq)-len(motif)+1):
    sub = seq[i:i+len(motif)]
    # print(sub) #uncomment to print chunks of motif size
    if sub == motif:
        matches.append(i+1)

for i in matches:
    print(i, end=" ")

print()

f.close()
