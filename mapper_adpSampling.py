#!/usr/bin/env python2.7

import sys
import math
import numpy as np
import scipy.spatial

K = 200
dim = 750

# How many candidates to sample for each round. Obviously 10dkln(1/epsion) is way too much.
beta = 200

# How many coresets to generate 
delta = 100

def find_nearest(array,value):
    dist = np.sum(np.square(np.abs(array-value)))
    min_dist = np.amin(dist)
    min_idx = dist.argmin()
    return min_dist, min_idx

if __name__ == "__main__":
    np.random.seed(seed = 42)
    data = []
    
    # For Test
    # data = np.load("samples_n_5000.npy")
        
    # For MapReduce, offline kmeans for coresets might not be a good idea
    for line in sys.stdin():
        line = line.strip()
        x = map(float, line.split())
        data.append(x)
    
    # transform to array type    
    data = np.array(data)
    sub_data = data
    
    candidates = np.array([])
    
    # Coreset construction
    sub_data_size = sub_data.shape[1]
    while sub_data_size > beta:
        # random sample with replacement. TODO: Should we also try that without replacement
        idx = np.random.randint(sub_data_size, size = beta)
        s = sub_data(idx.tolist())
        min_dist = np.zeros(sub_data_size)
        
        for i in range(sub_data_size):
            _, min_dist[i] = find_nearest(s, sub_data[i])
        
        if candidates.shape[0] == 0:
            candidates = s
        else:
            candidates = np.vstack((candidates, s))
        
        # Remove half of the codes
        num_reduced = math.ceil(sub_data_size/2)
        sub_data = np.sort(min_dist)[num_reduced:-1]
        sub_data_size = sub_data.shape[0]
        
    if candidates.shape[0] == 0:
            candidates = sub_data
    else:
            candidates = np.vstack((candidates, sub_data))
        
    # Calculate Voroni graph  
    dist = scipy.spatial.distance.cdist(data, candidates)
    idx = np.argmin(dist, axis = 1)
    
    weight = np.zeros(data.shape[0])
    
    # Update weights for each candidates
    for i in range(candidates):
        idx_group = np.where(idx == i)[0]
        group_size = idx_group.shape[0]
        sum_group_dist = np.sum(dist[:, idx_group.tolist()])
        
        for j in range(group_size):
            weight[idx_group[j]] = math.ceil((5. / group_size) + \
                                             (dist[idx_group[j], i] / sum_group_dist))
        
    # Importance sampling according to the weights
    sum_weight = np.sum(weight)
     
    prob = weight / float(sum_weight)          
    
    coreset_idx = np.random.choice(data.shape[0], delta, prob)
    
    coreset = data[coreset_idx]
    
    weight = 1. / (prob[coreset_idx]*delta)
    
    for c, w in zip(coreset, weight):
        key1 = "1\t" # just a dummy key
        key2 = str(w) + " "
        point = np.array_str(c)[1:-1]
        print key1 + key2 + point
        
        