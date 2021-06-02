#!/usr/bin/python3
import sys
import math


args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open("weights.txt", 'rt')
except:
    print('File Not Found!')
    sys.exit()


weightsDict = {}



for line in f:
    split_line = line.strip().split("   ")
    weightsDict[split_line[0]] = float(split_line[1])

f.close()

try:
     aa_seq = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()

seq = aa_seq.readline().strip()

mw = 0
for aa in seq:
    mw +=  weightsDict[aa]

print(round(mw, 3))


aa_seq.close()
