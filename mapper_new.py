#!/usr/bin/env python2.7

import numpy as np
import sys
#from scipy.spatial import Voronoi

k = 200
dim = 750
count = 0
csize = 600
#Data = []
w = [0 for j in range(csize)]

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
        sys.stderr.write(str(count)+'\t')
        if count > csize:
            D = np.tile(x, (csize,1))
            tmp = np.square(np.subtract(Data, D))
            s = tmp.sum(axis=1)
            center = np.argmax(s)
            w[center] = w[center] + 1
        else:
            #Data = np.concatenate((Data, x), axis=0)
            if count == 1:
                Data = x
            else:
                Data = np.vstack([Data,x])
    coresets(Data)

