#!/usr/bin/env python2.7

import numpy as np
import sys
#from scipy.spatial import Voronoi

k = 200
dim = 750
count = 0
#csize = 1000
threshold = 2200
#Data = []

myu = [[0 for j in range(dim)] for i in range(k)]

def coresets(D):
    for i in range(csize):
        print "%d\t%d\t" % (np.random.random_integers(csize*10), w[i]),
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
        if count == 1:
            Data = x
            csize = 1
            w = np.array([1])
        else:
            D = np.tile(x, (csize,1))
            tmp = np.square(np.subtract(Data, D))
            s = tmp.sum(axis=1)
            center = np.argmin(s)
            value = np.min(s)
            #sys.stderr.write(str(center)+' '+str(value)+'\t')
            if value > threshold:
                w = np.append(w,1)
                csize = csize + 1
                Data = np.vstack([Data,x])
            else:
                w[center] = w[center] + 1
        sys.stderr.write(str(count)+' '+str(csize)+'\t')
    coresets(Data)

