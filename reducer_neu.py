#!/usr/bin/env python2.7

import sys
import numpy as np

k = 200
dim = 750
myu = np.zeros(shape = (k, dim))
nW = np.zeros(k)
x = []
cc = 0
batch = 100
tik = 0
c = np.zeros(batch)

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
        key2 ,feature = line.split("\t")
        x = np.array(feature.split()).astype(np.float)
        key2 = int(key2)
        if cc < k:
            myu[cc] = x
            nW[cc] = 1
        else:
            c[tik] = find(x)
            if tik == batch - 1:
                for j in range(batch):
                    tmp = myu[c[j]]
                    nW[c[j]] += 1
                    myu[c[j]] = np.add(tmp, np.multiply(np.subtract(x,tmp), 1 / nW[c[j]]))
                tik = -1
            tik += 1
        cc += 1
    for i in range(0, k, 1):
        for j in range(0, dim, 1):
            print "%f " % (myu[i][j]),
        print ""
