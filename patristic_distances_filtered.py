#! /usr/bin/env python3
'''
based on Niema Moshiri 2017
Compute all patristic distances from the given tree at a certain threshold
'''
import argparse
from sys import stdin,stdout
from treeswift import read_tree_newick

# parse arguments
def parseArgs():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=argparse.FileType('r'), default=stdin, help="Input FASTA")
    parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'), default=stdout, help="Output, don't include file type")
    parser.add_argument('-t', '--threshold', required=False, type=int, default=1, help="Threshold")
    args = parser.parse_args()
    return args.input, args.output, args.threshold

# main code execution
infile, outfile, t = parseArgs()
dm = read_tree_newick(infile.read()).distance_matrix()
infile.close()
outfile = str(outfile) + ".txt"
outfile_filtered = str(outlife) + ".filtered.txt"
keys = list(dm.keys())
for i in range(len(keys)-1):
    for j in range(i+1,len(keys)):
        outfile.write('%f\n'%dm[keys[i]][keys[j]])
        if dm[keys[i]][keys[j]] <= t:
            outfile_filtered.write('%f\n'%dm[keys[i]][keys[j]])
