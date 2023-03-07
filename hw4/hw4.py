import csv
import numpy as np
from numpy import linalg as LA
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

def load_data(filepath):
    d = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            d.append(row)
    return d

def calc_features(row):
    return np.array([int(row['Attack']), int(row['Sp. Atk']), int(row['Speed']), int(row['Defense']), int(row['Sp. Def']), int(row['HP'])])

def hac(features):
    final = []
    temp = []
    maxInd = len(features)
    di = {}
    for i in range (len(features)):
        a = []
        di[i] = 1
        a.append(i)
        a.append(features[i])
        temp.append(a)

    while len(temp) > 1:
        minDist = 10000
        c1, c2 = [],[]
        i1, i2 ,d1,d2,k1,k2 = 0,0,0,0,0,0
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                    maxDist = 0
                    for k in range (1,len(temp[i])):
                        for p in range (1,len(temp[j])):
                            dist = LA.norm(temp[i][k] - temp[j][p])
                            if dist>maxDist:
                                maxDist=dist
                                k1 = k
                                k2 = p
                    if maxDist < minDist:
                        minDist = maxDist
                        c1 = temp[i][k1]
                        i1 = temp[i][0]
                        c2 = temp[j][k2]
                        i2 = temp[j][0]
                        d1 = i
                        d2 = j
        nc = [maxInd, c1, c2]
        di[maxInd] = di[i1] + di[i2]
        maxInd += 1
        final.append([i1, i2, minDist, di[maxInd-1]])
        temp.append(nc)
        del temp[d1]
        if d1<d2:
            del temp[d2-1]
        else:
            del temp[d2]

    return np.array(final)

def imshow_hac(Z):
    dn = dendrogram(Z)
    plt.show()
