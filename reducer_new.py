#!/usr/bin/env python2.7

import sys
import numpy as np
from time import time
from sklearn.cluster import KMeans

k = 200
dim = 750
myu = np.zeros(shape = (k, dim))
count = 0
x = []
cc = 0


def findin(Element):
    xx = np.tile(Element,(k,1))
    tmp = np.square(np.subtract(myu,xx))
    s = tmp.sum(axis=1)
    center = np.argmin(s)
    return center

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key2 ,feature = line.split("\t")
        x = np.array(feature.split()).astype(np.float)
        key2 = float(key2)
        if cc == 0 :
            key = np.array(key2)
            Data = np.array(x)
        else:
            key = np.append(key, key2)
            Data = np.vstack([Data, x])
        cc += 1
    for i in range(k):
        myu[i] = Data[i]
    t0 = time()
    km = KMeans(init = 'k-means++', n_clusters = k, precompute_distances = True, max_iter = 40)
    km.fit(Data)
    myu = np.array(km.cluster_centers_)
    for i in range(0, k, 1):
        for j in range(0, dim, 1):
            print "%f " % (myu[i][j]),
        print ""


"""
    for iteration in range(40):
        sys.stderr.write(str(iteration)+'\t')
        #count = 0
        myu2 = np.zeros(shape = (k,dim))
        kk = np.zeros(shape=(k,1))
        for i in range(len(Data)):
            xx = np.tile(Data[i],(k,1))
            tmp = np.square(np.subtract(myu,xx))
            s = tmp.sum(axis=1)
            c = np.argmin(s)
            myu2[c] = np.add(myu2[c],np.multiply(Data[i],key[i]))
            kk[c] += key[i]
        for i in range(k):
            myu[i] = np.divide(myu2[i],kk[i])
        #tmp = myu[c]
        #myu[c] = np.add(np.multiply(tmp, count / (count + key[i])), np.multiply(Data[i], key[i] /(count+key[i])))
        #    count += key[i]
"""

