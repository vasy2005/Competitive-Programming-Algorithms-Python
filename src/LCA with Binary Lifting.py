from collections import defaultdict

#Constants
NMAX = 100005

#Variables
l = defaultdict(list)
dp = [[0]*20 for _ in range(NMAX)]
_in = [0]*NMAX
out = [0]*NMAX
f = [0]*NMAX
counter = 0
queries = []

#Functions
def Read(fin):
    global n, m
    n, m = map(int, fin.readline().split())
    aux = list(map(int, fin.readline().split()))
    for i in range(2, n+1):
        dp[i][0] = aux[i-2]
        l[dp[i][0]].append(i)

    for i in range(1, m+1):
        x, y = map(int, fin.readline().split())
        queries.append((x, y))

def BinaryLiftingInit():
    global n, map
    for j in range(1, 19):
        for i in range(1, n+1):
            dp[i][j] = dp[dp[i][j-1]][j-1]

def LCA(x, y):
    if (is_ancestor(x, y)):
        return x
    if (is_ancestor(y, x)):
        return y

    for i in range(18, -1, -1):
        if (is_ancestor(dp[x][i], y) == 0):
            x = dp[x][i]

    return dp[x][0]

def is_ancestor(x, y):
    if (x == 0 or x == y):
        return 1

    return (_in[x] < _in[y] and out[x] > out[y])

def DFS(vf):
    global counter
    f[vf] = 1
    counter += 1; _in[vf] = counter
    for vfnou in l[vf]:
        if (f[vfnou] == 0):
            DFS(vfnou)
    counter += 1; out[vf] = counter


#Main
with open('input.in', 'r') as file:
    Read(file)

BinaryLiftingInit()

DFS(1)

with open('output.out', 'w') as fout:
    for i in range(m):
        fout.write(str(LCA(queries[i][0], queries[i][1]))+'\n')