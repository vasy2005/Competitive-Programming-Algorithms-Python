#pbinfo Prim


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

for vfnou in l[start]:
    dmin[vfnou[0]] = vfnou[1]

f = [0] * (n+1)

suma = 0
f[start] = 1
dmin[start] = 0; tata[start] = 0;
for i in range(1, n):
    minim = INF; vfmin = 0
    for j in range(1, n+1):
        if not f[j] and minim > dmin[j]:
            minim = dmin[j]
            vfmin = j

    f[vfmin] = 1; suma += minim
    for vfnou in l[vfmin]:
        vf = vfnou[0]; cost = vfnou[1]
        if not f[vf] and dmin[vf] > cost:
            dmin[vf] = cost
            tata[vf] = vfmin

with open('../.venv/prim.out', 'w') as file:
    file.write(str(suma) + '\n')
    for i in range(1, n+1):
        file.write(str(tata[i]) + ' ')