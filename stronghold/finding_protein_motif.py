#!/usr/bin/env python3


import sys
import requests
import re
query_parameters = {"downloadformat": "fasta"}


try:
    accessions_file = open("rosalind_mprt.txt", 'rt')
except:
    print("File Not Found!")
    sys.exit()


accession_seqs = {}

for accession in accessions_file:
    access_id = accession[:6]
    url = f'http://www.uniprot.org/uniprot/{access_id}.fasta'
    response = requests.get(url, params=query_parameters)
    if response.ok:
        preprocess = response.content.decode('utf-8').split('\n')[1:]
        accession_seqs[accession] = ''.join(preprocess)
        

motif = r'(?=([N][^P][S|T][^P]))'
for id, prot_seq in accession_seqs.items():
    search = re.search(motif, prot_seq)
    if search is not None:
        print(id, end ='')
        for match in re.finditer(motif, prot_seq):
            print(match.start()+1, end=' ')
        print()


accessions_file.close()

