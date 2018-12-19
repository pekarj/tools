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
    parser.add_argument('-i', '--input', required=False, type=argparse.FileType('r'), default=stdin, help="Input tree")
    parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'), default=stdout, help="Output, don't include file type")
    parser.add_argument('-t', '--threshold', required=False, type=float, default=1, help="Threshold")
    args = parser.parse_args()
    return args.input, args.output, args.threshold

# main code execution
infile, outfile, t = parseArgs()
dm = read_tree_newick(infile.read()).distance_matrix()
infile.close()
keys = list(dm.keys())
for i in range(len(keys)-1):
    for j in range(i+1,len(keys)):
        if dm[keys[i]][keys[j]] <= t:
            outfile.write('%s,%s,%f\n'%(keys[i],keys[j],dm[keys[i]][keys[j]]))
