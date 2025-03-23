import heapq

INF = 10000005

with open('../.venv/prim.in', 'r') as file:
    line = file.readlines()
    n, m = [int(x) for x in line[0].split()]

start = 1

l = [[] for _ in range(n+1)]
for i in range(1, m+1):
    x, y, cost = [int(x) for x in line[i].split()]
    l[x].append((y, cost))
    l[y].append((x, cost))

dmin = [INF] * (n+1)
tata = [start] * (n+1)
f = [False] * (n+1)

suma = 0;
dmin[start] = 0; tata[start] = 0
s = []
heapq.heappush(s, (dmin[start], start))
while s:
    minim, vfmin = heapq.heappop(s)

    if f[vfmin]:
        continue

    f[vfmin] = True
    suma += minim
    for vf, cost in l[vfmin]:
        if not f[vf] and dmin[vf] > cost:
            dmin[vf] = cost
            tata[vf] = vfmin
            heapq.heappush(s, (dmin[vf], vf))

with open('../.venv/prim.out', 'w') as file:
    file.write(str(suma) + '\n')
    for i in range(1, n+1):
        file.write(str(tata[i]) + ' ')