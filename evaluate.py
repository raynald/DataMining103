#!/usr/bin/env python2.7

import sys
import numpy as np
import scipy.spatial

K = 200
dim =750

def find_nearest(array,value):
    dist = scipy.spatial.distance.cdist(value, array)
    min_dist = np.amin(dist, axis = 1)
    min_idx = dist.argmin(axis = 1)
    return min_dist, min_idx

data = np.load("../data/samples_n_10000.npy")

centers = np.zeros(shape = (K, dim))

count = 0

f = open('centers.txt', 'r+')

for line in f:    
    centers[count] = np.array(line.split()).astype(np.float)
    count += 1

min_dist, _ = find_nearest(centers, data)

sum_dist = np.sum(np.square(min_dist)) / data.shape[0]

print sum_dist