#!/usr/bin/env python2.7

import logging
import sys

import numpy as np

k = 200
dim = 750

if __name__ == "__main__":
    #if not len(sys.argv) == 1:
    #    logging.error("Usage: evaluate.py myu.txt")
    #    sys.exit(1)

    data = np.load("/tmp/arr_0.npy")

    with open(sys.argv[1], "r") as fp_weights:
        weights = np.genfromtxt(fp_weights).flatten()

    accuracy = 0
    total = 0
    for nu in range(0, 100000, 1):
        ans = -1
        s = 0
        for i in range(k):
            s = np.square(np.subtract(np.array(ata[nu])) - weights[i*dim:(i+1)*dim:1])
            if ans == -1 or s < ans:
                ans = s
        total = total + ans
    ans /= 100000.0

    print("%f" % ans)
