# Fusing an external sequence with a viral sequence in a fasta file to make a sequence with ambigs in that fasta file.

import os
import subprocess
import numpy as np
import pandas as pd
from Bio import SeqIO
from treeswift import read_tree_newick
