#!/usr/bin/env python2.7

import sys
import numpy as np

k = 200
dim = 750
csize = 2000
myu = [[0 for j in range(dim)] for i in range(k)]
count = 0
x = []


def find(Element):
    Ans = -1
    Ansj = 0
    for i in range(0, k, 1):
        Sum = 0
        for j in range(0, dim, 1):
            Sum += (myu[i][j] - int(Element[j])) * (myu[i][j] - int(Element[j]))
        if Ans == -1 or Sum < Ans:
            Ans = Sum
            Ansj = i
    return Ansj

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key1, key2 ,feature = line.split("\t")
        x = feature.split()
        key1 = int(key1)
        key2 = int(key2)
        c = find(x)
        for i in range(dim):
            myu[c][i] = count / (count+int(key2)) * myu[c][i] + int(key2) / (count+int(key2)) * int(x[i])
            count += int(key2)
    for i in range(0, k, 1):
        for j in range(0, dim, 1):
            print "%f " % (myu[i][j]),
        print ""
