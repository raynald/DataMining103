#!/usr/bin/env python2.7

import sys
import numpy as np
from time import time
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

k = 200
dim = 750
myu = np.zeros(shape = (k, dim))
count = 0
x = []
cc = 0
data = []
Key = []


def findin(Element):
    xx = np.tile(Element,(k,1))
    tmp = np.square(np.subtract(myu,xx))
    s = tmp.sum(axis=1)
    center = np.argmin(s)
    return center

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key ,feature = line.split("\t")
        #x = np.array(feature.split()).astype(np.float)
        x = map(float, feature.split())
        key2 = float(key)
        Key.append(key2)
        data.append(x)
        cc += 1
    Data = np.array(data)
    key = np.array(key)
    for i in range(k):
        myu[i] = Data[i]
    t0 = time()
    #km = KMeans(init = 'k-means++', precompute_distances = True , n_clusters = k)
    km = MiniBatchKMeans(init = 'k-means++', batch_size = 500, n_clusters = k)
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

