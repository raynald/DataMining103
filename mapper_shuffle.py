#!/usr/bin/env python2.7

import sys
import numpy as np


K = 200
dim = 750

if __name__ == "__main__":
    np.random.seed(seed = 42)
    
    # For Test
    data = np.load("../data/arr_0.npy")
        
#     # For MapReduce, offline kmeans for coresets might not be a good idea
#     for line in sys.stdin():
#         line = line.strip()
#         x = map(float, line.split())
#         data.append(x)
#     
#     # transform to array type    
#     data = np.array(data)

    idx = np.random.permutation(data.shape[0])
    data = data[idx.tolist()]
    
    weight = 1
    
#     for i in range(10000):
#         key1 = "1\t" # just a dummy key
#         key2 = str(weight) + ", "
#         fea = str(data[i].tolist()).strip('[]')
#         print key1 + key2 + fea
    for i in range(10000):
        fea = str(data[i].tolist()).strip('[]').replace(',', '')
        print fea  
        