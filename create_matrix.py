#!/usr/bin/env python
__author__ = 'dtalessi'

from sklearn.cluster import KMeans
from sklearn import cluster
import sys
from numpy import vstack
from scipy import sparse


def parse_file(file_name):
    f = open(file_name, 'r')
    matrix = []
    for line in f:
        line = line.strip().split('\t')
        line = [int(i) for i in line]
        matrix.append(line)
        print(len(line))
    matrix = sparse.hstack(matrix)
    return matrix



def main(input_file):
    matrix = parse_file(input_file)
    k_means = cluster.KMeans()
    k_means.fit(matrix)


if __name__ == '__main__':
    main(*sys.argv[1:])




