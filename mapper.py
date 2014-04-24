#!/usr/bin/env python2.7

import numpy as np
import sys

k = 200
dim = 750
count = 0
#eta = 0.1

myu = [[0 for j in range(dim)] for i in range(k)]

def find(Element):
    Ans = -1
    Ansj = 0
    for i in range(0, k, 1):
        Sum = 0
        for j in range(0, dim, 1):
            Sum += (myu[i][j] - Element[j]) * (myu[i][j] - Element[j])
        if Ans == -1 or Sum < Ans:
            Ans = Sum
            Ansj = i
    return Ansj

if __name__ == "__main__":
    np.random.seed(seed=42)

    data = np.load("arr_0.npy")

    for nu in range(0, 30, 1):#len(data),1):
        line = data[nu]
        #x = np.fromstring(line, sep = " ")
        x = line
        count = count + 1
        c = find(x)
        for i in range(0, dim, 1):
            myu[c][i] = myu[c][i] + 1.0 / count * (x[i] - myu[c][i])
    for i in range(0, dim, 1):
        for j in range(0, k, 1):
            print "%d\t%d\t%d" % (j, i, myu[j][i])
