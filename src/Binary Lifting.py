import numpy as np

#Constants
NMAX = 250005
LOGMAX = 20

#Variables
dp = np.zeros((NMAX, LOGMAX), dtype=int)
queries = []

#Functions
def Read(fin):
    global n, m
    n, m = map(int, fin.readline().split())

    values = list(map(int, fin.readline().split()))
    for i in range(1, n+1):
        x = values[i-1]
        dp[i, 0] = x

    for i in range(1, m+1):
        q, p = map(int, fin.readline().split())
        queries.append((p, q))

def BinaryLiftingPrecalc():
    for j in range(1, 19):
        for i in range(1, n+1):
            dp[i, j] = dp[dp[i, j-1], j-1]

def BinaryLifting(p, q):
    for i in range(18, -1, -1):
        if ((p>>i)&1 == 1):
            q = dp[q, i]
    return q

#Main
with open('stramosi.in', 'r') as fin:
    Read(fin)

BinaryLiftingPrecalc()

with open('stramosi.out', 'w') as fout:
    for i in range(m):
        ans = BinaryLifting(queries[i][0], queries[i][1])
        fout.write(str(ans)+'\n')


