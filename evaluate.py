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

    data = np.load("arr_0.npy")

    with open(sys.argv[1], "r") as fp_weights:
        weights = np.genfromtxt(fp_weights).flatten()

    accuracy = 0
    total = 0
    for nu in range(0, 10000, 1):
        sys.stderr.write(str(nu)+'\t')
        ans = -1
        for i in range(k):
            ss = np.sum(np.square(np.subtract(np.array(data[nu]), weights[i*dim:(i+1)*dim:1])))
            if ans == -1 or ss < ans:
                ans = ss
        total = total + ans
    total /= 10000.0

    print("%f" % total)
