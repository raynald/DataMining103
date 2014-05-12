#!/usr/bin/env python2.7

from time import time
import numpy as np
import sys
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

k = 100
dim = 750
count = 0
data = []
#csize = 200
#Data = []
#w = [0 for j in range(csize)]

myu = [[0 for j in range(dim)] for i in range(k)]

def coresets(D):
    for i in range(k):
            print "%d\t" % 1,
            for j in range(dim-1):
                print "%f" % D[i][j],
            print "%f" % D[i][dim-1]

if __name__ == "__main__":
    np.random.seed(seed=42)

    for line in sys.stdin:
        line = line.strip()
        #line = data[nu]
        #x = np.fromstring(line, sep = " ")
        #x = line
        x = map(float, line.split())
        data.append(x)
        count = count + 1
        sys.stderr.write(str(count)+'\t')
    Data = np.array(data)
    np.random.shuffle(Data)
    k = count
    coresets(Data)
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
