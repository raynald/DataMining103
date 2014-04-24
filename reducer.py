#!/usr/bin/env python2.7

import sys
import numpy as np

k = 200
dim = 750
le = [[0 for j in range(dim)] for i in range(k)]
d = [[0 for j in range(dim)] for i in range(k)]

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key1, key2, myu = np.fromstring(line, sep = "\t")
        key1 = int(key1)
        key2 = int(key2)
        le[key1][key2] = le[key1][key2] + 1
        d[key1][key2] = d[key1][key2] + float(myu)
    for i in range(0, k, 1):
        for j in range(0, dim, 1):
            print "%f" % (d[i][j] * 1.0 / le[i][j]),
        print ""
