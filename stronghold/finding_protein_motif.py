#!/usr/bin/env python3


import sys
import requests
query_parameters = {"downloadformat": "fasta"}


try:
    accessions_file = open("protein_motifs.txt", 'rt')
except:
    print("File Not Found!")
    sys.exit()


accession_seqs = {}

for accession in accessions_file:
    access_id = accession[:6]
    url = f'http://www.uniprot.org/uniprot/{access_id}.fasta'
    response = requests.get(url, params=query_parameters)
    if response.ok:
        #preprocess_seq = response.contant.split("\n")
        accession_seqs[access_id] = response.content.rstrip()

for id, prot_seq in accession_seqs.items():
    #preprocess_seq = prot_seq
    print(prot_seq)