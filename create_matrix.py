#!/usr/bin/env python
__author__ = 'dtalessi'

from sklearn.cluster import KMeans
from sklearn import cluster
import sys
import numpy as np
from Bio.Cluster import kcluster
from scipy import sparse


def parse_file(file_name):
    f = open(file_name, 'r')
    matrix = []
    for line in f:
        line = line.strip().split('\t')
        line = [int(i) for i in line]
        matrix.append(line)
        print(len(line))
    #matrix = sparse.hstack(matrix)
    matrix = np.array(matrix)
    return matrix



def main(input_file):
    matrix = parse_file(input_file)
    clusterid, error, nfound = kcluster(matrix, nclusters=2) #change number of clusters
    clusterid = [str(i) for i in clusterid]
    clusters_as_string = "\n".join(clusterid)
    print(clusters_as_string)

    # k_means = cluster.KMeans()
    # answer = k_means.fit(matrix)
    # print answer
    # print answer.fit_predict(matrix)
    # visualize_cluster = answer.transform(matrix)
    # f = open("Kmeans_" + "learning_topology" + ".out", "w")
    # for row in visualize_cluster:
    #     row = [str(i) for i in row]
    #     row_to_string = "\t".join(row)
    #     f.write(row_to_string + "\n")
    # f.close()

if __name__ == '__main__':
    main(*sys.argv[1:])




