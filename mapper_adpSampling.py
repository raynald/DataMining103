#!/usr/bin/env python2.7

import sys
import math
import numpy as np
import scipy.spatial

K = 200
dim = 750

# How many candidates to sample for each round. Obviously 10dkln(1/epsion) is way too much.
beta_ratio = 0.03

# How many coresets to generate 
delta_ratio = 0.015

def find_nearest(array,value):
    dist = scipy.spatial.distance.cdist(value, array)
    min_dist = np.amin(dist, axis = 1)
    min_idx = dist.argmin(axis = 1)
    return min_dist, min_idx

if __name__ == "__main__":
    np.random.seed(seed = 42)
    data = []
    
    # For Test
#     data = np.load("../data/samples_n_10000.npy")
#     idx = np.random.permutation(data.shape[0])[0:10000]
#     data = data[idx.tolist()]

    # For MapReduce, offline kmeans for coresets might not be a good idea
    for line in sys.stdin:
        line = line.strip()
        x = map(float, line.split())
        data.append(x)
     
    # transform to array type    
    data = np.array(data)
    
    beta = int(beta_ratio*data.shape[0])
    delta = int(delta_ratio*data.shape[0])
    sub_data = data
    
    candidates = np.array([])
    
    # Coreset construction
    sub_data_size = sub_data.shape[0]
    while sub_data_size > beta:
        # random sample with replacement. TODO: Should we also try that without replacement
        idx = np.random.randint(sub_data_size, size = beta)
        s = sub_data[idx.tolist()]
        
        min_dist, _ = find_nearest(s, sub_data)
        
        if candidates.shape[0] == 0:
            candidates = s
        else:
            candidates = np.vstack((candidates, s))
        
        # Remove half of the codes
        num_reduced = math.ceil(sub_data_size/2)
        # In ascending order
        reduced_idx = np.argsort(min_dist)[num_reduced:]
        sub_data = sub_data[reduced_idx]
        sub_data_size = sub_data.shape[0]
        
    if candidates.shape[0] == 0:
            candidates = sub_data
    else:
            candidates = np.vstack((candidates, sub_data))
        
    # Calculate Voroni graph  
    dist = np.square(scipy.spatial.distance.cdist(data, candidates))
    min_idx = np.argmin(dist, axis = 1)
    
    weight = np.zeros(data.shape[0])
    
    # Update weights for each candidates
    for i in range(candidates.shape[0]):
        idx_group = np.where(min_idx == i)[0]
        group_size = idx_group.shape[0]
        sum_group_dist = np.sum(dist[:, i ])
        
        for idx in idx_group:
            weight[idx] = math.ceil((5. / group_size) + \
                                             (dist[idx, i] / sum_group_dist))
        
    # Importance sampling according to the weights
    sum_weight = np.sum(weight)
     
    prob = weight / float(sum_weight)          
    
    coreset_idx = np.random.choice(data.shape[0], delta, replace=False, p=prob)
    
    coreset = data[coreset_idx]
    
    weight = 1. / (prob[coreset_idx]*delta)
    
    for c, w in zip(coreset, weight):
        key1 = "1\t" # just a dummy key
        key2 = str(w) + ", "
        fea = str(data[i].tolist()).strip('[]')
        print key1 + key2 + fea
        
        