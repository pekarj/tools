#! /usr/bin/env python3
'''
based on Niema Moshiri 2017
Compute all patristic distances from the given tree
'''
import argparse
from sys import stdin,stdout
from treeswift import read_tree_newick

# parse arguments
def parseArgs():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=argparse.FileType('r'), default=stdin, help="Input FASTA")
    parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'), default=stdout, help="Output")
    parser.add_argument('-t', '--threshold', required=False, type=int, default=1, help="Threshold")
    parser.add_argument('-o1', '--output1', required=False, type=argparse.FileType('w'), default=stdout, help="Filtered output")
    args = parser.parse_args()
    return args.input, args.output, args.threshold, args.output1

# main code execution
infile, outfile, t, outfile1 = parseArgs()
dm = read_tree_newick(infile.read()).distance_matrix()
infile.close()
keys = list(dm.keys())
for i in range(len(keys)-1):
    for j in range(i+1,len(keys)):
        outfile.write('%f\n'%dm[keys[i]][keys[j]])
        if dm[keys[i]][keys[j]] <= t:
            outfile1.write('%f\n'%dm[keys[i]][keys[j]])
