# Fusing an external sequence with a viral sequence in a fasta file to make a sequence with ambigs in that fasta file.

import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio import Seq
from treeswift import read_tree_newick
import argparse

# parse arguments
def parseArgs():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=argparse.FileType('r'), help="Input FASTA")
    parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'), help="Output")
    parser.add_argument('-r', '--randomIndex', required=False, type=float, default=None, help="Sequence to change in input")
    parser.add_argument('-e', '--externalSeq', required=False, type=argparse.FileType('r'), help="External sequence to incorporate")
    args = parser.parse_args()
    return args.input, args.output, args.randomIndex, args.externalSeq


# main code execution
infile, outfile, random_seq_index, external_seq = parseArgs()
seqs = readFASTA(infile)
infile.close()
  
ext_seq = list(SeqIO.parse(external_seq, "fasta"))[0]

for index, record in enumerate(SeqIO.parse(seqs, "fasta")):
    if index == random_seq_index:
        old_seq = record

#making a new seq
new_seq = ""
for i in range(len(old_seq.seq)):
    if i > len(hxb2.seq) - 1:
        new_seq += "-"
    else:
        # keeping the seq the same
        if hxb2.seq[i] == old_seq.seq[i]:
            new_seq += hxb2.seq[i]
        else:
            # adding the ambigs
            if ext_seq.seq[i] == "Y" or old_seq.seq[i] == "Y":
                new_seq += "Y"
            elif ext_seq.seq[i] == "R" or old_seq.seq[i] == "R":
                new_seq += "R"
            elif ext_seq.seq[i] == "W" or old_seq.seq[i] == "W":
                new_seq += "W"
            elif ext_seq.seq[i] == "S" or old_seq.seq[i] == "S":
                new_seq += "S"
            elif ext_seq.seq[i] == "K" or old_seq.seq[i] == "K":
                new_seq += "K"
            elif ext_seq.seq[i] == "M" or old_seq.seq[i] == "M":
                new_seq += "M"
            elif set(("C", "T")) == set((ext_seq.seq[i], old_seq.seq[i])):
                new_seq += "Y"
            elif set(("A", "G")) == set((ext_seq.seq[i], old_seq.seq[i])):
                new_seq += "R"
            elif set(("A", "T")) == set((ext_seq.seq[i], old_seq.seq[i])):
                new_seq += "W"
            elif set(("G", "C")) == set((ext_seq.seq[i], old_seq.seq[i])):
                new_seq += "S"
            elif set(("T", "G")) == set((ext_seq.seq[i], old_seq.seq[i])):
                new_seq += "K"
            elif set(("C", "A")) == set((ext_seq.seq[i], old_seq.seq[i])):
                new_seq += "M"


rec = SeqRecord(Seq.Seq(new_seq), 
                name=old_seq.name, 
                id=old_seq.name,
                description=old_seq.name)

records = []
for index, record in enumerate(SeqIO.parse(old_seqs_path, "fasta")):
    if index == random_seq_index:
        records.append(rec)
        print(index)
        print(rec.name)
    else:
        records.append(record)

SeqIO.write(records, 
            outfile,
            "fasta")
