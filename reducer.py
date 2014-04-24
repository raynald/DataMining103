#!/usr/bin/env python2.7

k = 200

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, myu = np.fromstring(line, sep = "\t")
        myu = np.fromstring(line, sep = " ")
        key = int(key)
        le[key] = le[key] + 1
        d[key][le[key]] = float(x)
    for i in range(0, k, 1):
        for j in range(0, dim, 0):

            print "%
