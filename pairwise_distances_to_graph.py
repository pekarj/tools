#!/usr/bin/env python3
'''
Convert pairwise distances to graph
'''

from gzip import open as gopen
from sys import stdin,stdout
import argparse
from networkx import Graph, graph_edit_distance, optimize_graph_edit_distance
import networkx as nx

# parse args
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i', '--input', required=False, type=str, default='stdin', help="Input (tn93 Output CSV")
parser.add_argument('-t', '--threshold', required=False, type=float, default=float('inf'), help="Distance Threshold")
parser.add_argument('-o', '--output', required=False, type=str, default='stdout', help="Output File")
args,unknown = parser.parse_known_args()
assert args.threshold >= 0, "ERROR: Length threshold must be at least 0"
if args.input == 'stdin':
    args.input = stdin
elif args.input.lower().endswith('.gz'):
    args.input = gopen(args.input)
else:
    args.input = open(args.input)
if args.output == 'stdout':
    args.output = stdout
else:
    args.output = open(args.output,'w')

# build graph
g = Graph() 
for line in args.input:
    if "ID" in line:
        continue
    u,v,d = line.strip().split(","); d = float(d)
    if u not in g:
        g.add_node(u)
    if v not in g:
        g.add_node(v)
    if d <= args.threshold:
        g.add_edge(u,v,length=d)

nx.write_gpickle(g, args.output)
