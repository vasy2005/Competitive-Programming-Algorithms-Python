#pbinfo Prim
from collections import defaultdict
import heapq

#Constants
NMAX = 105
INF = 1000000005

#Variables
l = defaultdict(list)
dmin = [INF] * NMAX
f = [False] * NMAX
start = 1;
tata = [start] * NMAX
heap = []
suma = 0

#Functions
def Read(fin):
    global n, m
    n, m = map(int, fin.readline().split())
    for i in range(m):
        x, y, cost = map(int, fin.readline().split())
        l[x].append((y, cost))
        l[y].append((x, cost))

def Prim():
    global suma
    dmin[start] = 0; tata[start] = 0
    heapq.heappush(heap, (dmin[start], start))
    while (len(heap) > 0):
        aux = heapq.heappop(heap)
        minim = aux[0]; vfmin = aux[1]

        if (f[vfmin] == True):
            continue;

        f[vfmin] = True; suma += minim
        for vfnou in l[vfmin]:
            vf = vfnou[0]; cost = vfnou[1]
            if not f[vf] and dmin[vf] > cost:
                dmin[vf] = cost
                tata[vf] = vfmin
                heapq.heappush(heap, (dmin[vf], vf))

#Main
with open('input.in', 'r') as fin:
    Read(fin)

Prim()

with open('output.out', 'w') as fout:
    fout.write(f"{suma}\n")
    for i in range(1, n+1):
        fout.write(f"{tata[i]} ")