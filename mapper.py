#!/usr/bin/env python2.7

import numpy as np
import sys
#from scipy.spatial import Voronoi

k = 200
dim = 750
count = 0
csize = 600
Data = []
w = [0 for j in range(csize)]

myu = [[0 for j in range(dim)] for i in range(k)]

def coresets(D):
    B = []
    D_p = D
    sample = []
    #while len(D_p) != 0:
    for i in range(csize):
        tmp = np.random.random_integers(len(D)-1)
        sample += [tmp]
    for i in range(len(D)):
        sys.stderr.write(str(i)+'\t')
        maxh = -1
        for j in range(csize):
            tmp = np.sum(np.square(np.subtract(np.array(D[i]),np.array(D[sample[j]]))))
            if tmp < maxh or maxh == -1:
                maxh = tmp
                ans = j
        w[ans] = w[ans] + 1
    for i in range(csize):
        print "%d\t%d\t" % (np.random.random_integers(csize*csize), w[i]),
        for j in range(dim-1):
            print "%f" % D[sample[i]][j],
        print "%f" % D[sample[i]][dim-1]

if __name__ == "__main__":
    np.random.seed(seed=42)

    #data = np.load("arr_0.npy")

    #for nu in range(0, 10000,#len(data),1):
    for line in sys.stdin:
        line = line.strip()
        #line = data[nu]
        x = np.fromstring(line, sep = " ")
        #x = line
        count = count + 1
        Data = Data + [x]
    coresets(Data)
