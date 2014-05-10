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

    wei = np.array(weights[0:dim])
    for i in range(1,k,1):
        wei = np.vstack([wei,weights[i*dim:(i+1)*dim]])
    accuracy = 0
    total = 0
    for nu in range(0, 7000, 1):
        sys.stderr.write(str(nu)+'\t')
        xxx = np.tile(data[nu],(k,1))
        tmp = np.square(np.subtract(xxx,wei))
        s = tmp.sum(axis=1)
        sss = np.min(s)
        total = total + sss
    total /= 7000.0

    print("%f" % total)
