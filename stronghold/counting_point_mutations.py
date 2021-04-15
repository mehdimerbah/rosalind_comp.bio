#!/usr/bin/python3
import sys

args = sys.argv
if len(args) == 1:
    print("Please Specify filename")
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print("File Not Found!")
    sys.exit()


line1 = f.readline()
line2 = f.readline()

count = 0

for itr1, itr2 in zip(line1, line2):
    if itr1 != itr2:
        count+=1

print(count)

f.close()
