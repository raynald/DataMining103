#!/usr/bin/env python2.7

from time import time
import numpy as np
import sys
from sklearn.cluster import KMeans

k = 100
dim = 750
count = 0
#csize = 200
#Data = []
#w = [0 for j in range(csize)]

myu = [[0 for j in range(dim)] for i in range(k)]

def coresets(D):
    for i in range(k):
        print "%d\t" % kk[i],
        for j in range(dim-1):
            print "%f" % D[i][j],
        print "%f" % D[i][dim-1]

if __name__ == "__main__":
    np.random.seed(seed=42)

    #data = np.load("arr_0.npy")

    #sample = np.random.randint(len(D),size=csize)
    #for nu in range(0, 10000,#len(data),1):
    for line in sys.stdin:
        line = line.strip()
        #line = data[nu]
        x = np.fromstring(line, sep = " ")
        #x = line
        count = count + 1
        sys.stderr.write(str(count)+'\t')
        if count == 1:
            Data = np.array(x)
        else:
            Data = np.vstack([Data,x])
    for i in range(k):
        myu[i] = Data[i]
    t0 = time()
    for iteration in range(10):
        sys.stderr.write(str(iteration)+'\t')
        #count = 0
        myu2 = np.zeros(shape = (k,dim))
        kk = np.zeros(shape=(k,1))
        for i in range(len(Data)):
            xx = np.tile(Data[i],(k,1))
            tmp = np.square(np.subtract(myu,xx))
            s = tmp.sum(axis=1)
            c = np.argmin(s)
            myu2[c] = np.add(myu2[c], Data[i])
            kk[c] += 1
        for i in range(k):
            myu[i] = np.divide(myu2[i],kk[i])
        #tmp = myu[c]
        #myu[c] = np.add(np.multiply(tmp, count / (count + key[i])), np.multiply(Data[i], key[i] /(count+key[i])))
        #    count += key[i]
    for i in range(k):
        sys.stderr.write(str(kk[i])+'\n')
    coresets(myu)
    sys.stderr.write(str(time()-t0)+'\n')
"""
    km = KMeans(init = 'k-means++', n_clusters = k, precompute_distances = True, max_iter = 20)
    km.fit(Data)
    myu = np.array(km.cluster_centers_)
    lab = np.array(km.labels_)
    kk = [0 for j in range(k)]
    for i in range(len(Data)):
        kk[lab[i]] += 1
    for i in range(k):
        sys.stderr.write(str(kk[i])+'\n')
    coresets(myu)
    sys.stderr.write(str(time()-t0)+'\n')
"""
