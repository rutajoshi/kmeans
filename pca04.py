#!/usr/bin/env python
__author__ = 'mmalessi'

import numpy as np
from Bio.Cluster import pca
import sys
from numpy import vstack



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
    f = open("pc_coordinates_" + "learning_topology" + ".out", "w")
    for row in coordinates:
        row = [str(i) for i in row]
        row_to_string = "\t".join(row)
        f.write(row_to_string + "\n")
    f.close()

if __name__ == '__main__':
    main(*sys.argv[1:])






