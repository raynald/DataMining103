#!/usr/bin/env python2.7

import sys
import numpy as np

k = 200
dim = 750
myu = np.zeros(shape = (k, dim))
count = 0
x = []
cc = 0


def find(Element):
    xx = np.tile(Element,(k,1))
    tmp = np.square(np.subtract(myu,xx))
    s = tmp.sum(axis=1)
    center = np.argmin(s)
    return center

if __name__ == "__main__":
    for line in sys.stdin:
        sys.stderr.write(str(cc)+'\t')
        line = line.strip()
        key1, key2 ,feature = line.split("\t")
        x = np.array(feature.split()).astype(np.float)
        key1 = int(key1)
        key2 = int(key2)
        if cc < k:
            myu[cc] = x
        else:
            c = find(x)
            tmp = myu[c]
            myu[c] = np.add(np.multiply(tmp, count / (count+1)), np.multiply(x, key2 /(count+1)))
        count += 1
        cc = cc + 1
    for i in range(0, k, 1):
        for j in range(0, dim, 1):
            print "%f " % (myu[i][j]),
        print ""
