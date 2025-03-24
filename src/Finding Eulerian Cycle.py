#infoarena Ciclu Eulerian

#Constants
NMAX = 1000005
NMAX = 5000005

#Variables
l = [[] for _ in range(NMAX)]
d = [0] * NMAX
f = [0] * NMAX
v = []
ans = []

#Functions
def Read(fin):
    global n, m
    global v
    (n, m) = (int(x) for x in fin.readline().split())
    for i in range(m):
        (x, y) = (int(x) for x in fin.readline().split())
        v.append((x, y))
        l[x].append(len(v)-1)
        l[y].append(len(v)-1)
        d[x] += 1; d[y] += 1


def eulerCycle(x):
    while (len(l[x]) > 0):
        ind = l[x][-1]; del l[x][-1]

        if (f[ind] == 0):
            f[ind] = 1

            if (v[ind][0] == x):
                y = v[ind][1]
            else:
                y = v[ind][0]

            eulerCycle(y)

    ans.append(x)

def gradPar():
    for i in range(1, n+1):
        if (d[i] % 2 == 1):
            return 0
    return 1


#Main
with open('ciclueuler.in', 'r') as fin:
    Read(fin)

if (gradPar() == 0):
    with open('ciclueuler.out', 'w') as fout:
        fout.write("-1\n")
    exit()

eulerCycle(1)

del ans[-1]

with open('ciclueuler.out', 'w') as fout:
    for i in ans:
        fout.write(f"{i} ")
    fout.write("\n")




