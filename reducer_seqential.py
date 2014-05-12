#!/usr/bin/env python2.7
import sys
import numpy as np

K = 200
dim = 750

def find_nearest_idx(array,value):
    idx = np.sum(np.square(np.abs(array-value))).argmin()
    return idx

if __name__ == "__main__":
    
    count = 0
    
    # K centers
    centers = np.zeros(shape = (K, dim))
    nCenters = np.zeros(K) # number of points assigned to each center        
    
    for line in sys.stdin:
        line = line.strip()
        key, val = line.split("\t")
        # val = weight, point features 
        val = np.array(val.split()).astype(np.float)
        weight = val[0]
        point = val[1:]
        
        # Initialize centers as the first K points arrived. TODO: definitely not an optimal solution
        if count < K:
            centers[count] = point
            idx = count
        else:
            idx = find_nearest_idx(centers, point)
                    
        count += 1
        nCenters[idx] += weight          
        
        # Update center i according to the number of effective points represented by the corset
        centers[idx] = centers[idx] + (point - centers[idx]) * (weight / nCenters[idx]) 

    # output centers
    for c in centers:
        print np.array_str(c)[1:-1]
             
        
        