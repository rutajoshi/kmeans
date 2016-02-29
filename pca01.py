#!/usr/bin/env python
__author__ = 'mmalessi'

import numpy as np
from sklearn.decomposition import PCA
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
    return matrix.toarray()



def main(input_file):
    matrix = parse_file(input_file)
    pca = PCA(n_components=2)
    pca.fit(matrix)
    print(pca.explained_variance_ratio_)

if __name__ == '__main__':
    main(*sys.argv[1:])




