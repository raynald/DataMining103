#!/usr/bin/env python2.7

import numpy as np

num = 10000; # How many samples to use 

# Load the file stored in NPZ format
data = np.load("../data/arr_0.npy")

# Use a random permutation to get the indices
sample_idx = np.random.permutation(data.shape[0]);

sample_idx = sample_idx[0:num]

samples = data[sample_idx.tolist()];

filename = "../data/samples_n_" + str(num)

np.save(filename, samples)

