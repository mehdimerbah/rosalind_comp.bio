#!/usr/bin/python3
import sys

args = sys.argv
if len(args) == 1:
    print("Please Specify filename")
    sys.exit()

f = open(args[1], 'rt')

def get_gc():            
    entries = {}
    for line in f:
        if '>' in line:
            seq_id = line.strip()[1:]
            entries[seq_id] = 0
        else:
            stripped = list(line.strip())
            g_count = stripped.count("G")
            c_count = stripped.count("C")
            gc_content = 100*(g_count+c_count)/len(stripped)
            entries[seq_id] = gc_content

    max_value = max(entries.values())
    index = list(entries.values()).index(max_value)
    print(entries)
    print(list(entries.keys())[index]," ",max_value,"%")

get_gc()

f.close()
