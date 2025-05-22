import heapq

INF = 100000005

with open('input.in', 'r') as file:
    line = file.readlines()

n, m = [int(x) for x in line[0].split()]
start = 1

l = [[] for _ in range(n+1)]
for i in range(1, m+1):
    x, y, cost = [int(x) for x in line[i].split()]
    l[x].append((y, cost))

cmin = [INF] * (n+1)
cmin[start] = 0

s = []
heapq.heappush(s, (0, start))
while (len(s) > 0):
    minim, vfmin = heapq.heappop(s)

    for vfnou in l[vfmin]:
        vf = vfnou[0]
        cost = vfnou[1]
        if (cmin[vf] > minim + cost):
            cmin[vf] = minim + cost
            heapq.heappush(s, (cmin[vf], vf))

for i in range(1, n+1):
    if (i == start):
        continue
    if (cmin[i] == INF):
        print('0', end=' ')
    else:
        print(f'{cmin[i]}', end=' ')

