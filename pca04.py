#!/usr/bin/env python
__author__ = 'mmalessi'

import numpy as np
from Bio.Cluster import pca
import sys
import operator
from numpy import vstack
from operator import itemgetter, attrgetter



def parse_file(file_name):
    f = open(file_name, 'r')
    matrix = []
    for line in f:
        line = line.strip().split('\t')
        line = [int(i) for i in line]
        matrix.append(line)
        print(len(line))
   # matrix = sparse.hstack(matrix)
    matrix = np.array(matrix)
    return matrix



def main(input_file):
    matrix = parse_file(input_file)
    columnmean, coordinates, pc, eigenvalues = pca(matrix)
    returns = columnmean, coordinates, pc, eigenvalues
    print_top_genes(returns)
    f = open("pc_coordinates_" + "learning_topology" + ".out", "w")
    for row in coordinates:
        row = [str(i) for i in row]
        row_to_string = "\t".join(row)
        f.write(row_to_string + "\n")
    f.close()

def print_top_genes(components, pc_num=0, num_genes=10):
    pc = components[pc_num]
    pc_abs = [(i, abs(pc[i])) for i in range(0, len(pc))]   # adding indices
    pc_abs.sort(key=operator.itemgetter(1))
    print("Top genes (PC" + str(pc_num) + "):")
    for i in range(0, num_genes):
        top_gene_index = pc_abs.pop()[0]
        print(top_gene_index + ": " + str(pc[top_gene_index]))


if __name__ == '__main__':
    main(*sys.argv[1:])






