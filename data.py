#!/usr/bin/env python2.7

import numpy as np
from sklearn.cluster import KMeans

# Load the file stored in NPZ format
#data = np.load("training.npz")['arr_0']
data = np.load("arr_0.npy")

for i in range(1000):
    for j in range(750):
        print data[i][j],
    print

# To store the file in CSV format
#np.savetxt('training.csv', data)

# Load CSV file
#data = np.loadtxt('training.csv')
