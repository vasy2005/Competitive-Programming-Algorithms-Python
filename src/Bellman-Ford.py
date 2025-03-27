import heapq
from collections import defaultdict

#Constants
NMAX = 50005
MMAX = 250005
INF = 100000005

#Variables
start = 1;
l = defaultdict(list)#l = [[] for _ in range(NMAX)]
dmin = [INF] * NMAX
neg = [0] * NMAX
heap = []
negativ = False

#Functions
def Read(fin):
    global x, y, cost
    global n, m
    n, m = map(int, fin.readline().split())
    for i in range(1, m+1):
        x, y, cost = map(int, fin.readline().split())
        l[x].append((y, cost))

#Main
with open('input.in', 'r') as fin:
    Read(fin)

dmin[start] = 0
heapq.heappush(heap, (0, start))
while len(heap) > 0 and not negativ:
    aux = heapq.heappop(heap)
    vfmin = aux[1]; minim = aux[0]

    for vfnou in l[vfmin]:
         vf = vfnou[0]; cost = vfnou[1]
         if dmin[vf] > minim+cost:
             dmin[vf] = minim+cost
             heapq.heappush(heap, (dmin[vf], vf))
             neg[vf] += 1
             if neg[vf] > n:
                 negativ = True
                 break

with open('output.out', 'w') as fout:
    if negativ:
        fout.write("Ciclu negativ!\n")
    else:
        for i in range(1, n+1):
            if i == start:
                continue
            if dmin[i] == INF:
                fout.write("0 ")
            else:
                fout.write(f"{dmin[i]} ")