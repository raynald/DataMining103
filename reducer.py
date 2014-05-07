#!/usr/bin/env python2.7

import sys
import numpy as np

k = 200
dim = 750
csize = 600
myu = [[0 for j in range(dim)] for i in range(k)]
count = 0
x = []
cc = 0


def find(Element):
    Ans = -1
    Ansj = 0
    for i in range(0, k, 1):
        Sum = 0
        for j in range(0, dim, 1):
            Sum += (myu[i][j] - float(Element[j])) * (myu[i][j] - float(Element[j]))
        if Ans == -1 or Sum < Ans:
            Ans = Sum
            Ansj = i
    return Ansj

if __name__ == "__main__":
    for line in sys.stdin:
        sys.stderr.write(str(cc)+'\t')
        line = line.strip()
        key1, key2 ,feature = line.split("\t")
        x = feature.split()
        key1 = int(key1)
        key2 = int(key2)
        if cc < k:
            for i in range(dim):
                myu[cc][i] = float(x[i])
        else:
            c = find(x)
            for i in range(dim):
                myu[c][i] = count / (count+key2) * myu[c][i] + key2 / (count+key2) * float(x[i])
        count += key2
        cc = cc + 1
    for i in range(0, k, 1):
        for j in range(0, dim, 1):
            print "%f " % (myu[i][j]),
        print ""
