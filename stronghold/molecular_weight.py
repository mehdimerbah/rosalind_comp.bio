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

    ######## Script ########
entries = {}
for line in f:
    if '>' in line:
        seq_id = line.strip()[1:]
        entries[seq_id] = []
    else:
        stripped = list(line.strip().strip("-").replace("-", "*"))

        #curr = list(entries[seq_id])
        entries[seq_id].extend(stripped)


AminoDict={ 'A':89.09, 'R':174.20, 'N':132.12, 'D':133.10, 'C':121.15, 'Q':146.15, 'E':147.13, 'G':75.07, 'H':155.16, 'I':131.17, 'L':131.17, 'K':146.19, 'M':149.21, 'F':165.19, 'P':115.13, 'S':105.09, 'T':119.12, 'W':204.23, 'Y':181.19, 'V':117.15, 'X':0.0, '-':0.0, '*':0.0 }

mw_dict = {}

for key in entries.keys():
    mw_dict[key] = 0

for key, val in entries.items():
    for i in val:
        mw_dict[key] += AminoDict[i]


for key, val in mw_dict.items():
   print("%20s : %4.3f" % (key, val))



#Create a dictionary that saves the molecualr weight of all proteins in a fasta file 
#Read the fasta file and define your dictionary as follows 
#The key should be the protein ID 
#the values should be the Molecular weight and the sequence 
# make sure the sequence does not have the "-" in it.


    ########################

f.close()
