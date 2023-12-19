#!/usr/bin/env python3

import sys

try:
    graph_file = open("graph_adj.txt", 'rt')
except:
    print("File Not Found!")
    sys.exit()


