#Constant Variables
NMAX = 100002

#Initialisation
di = [0] * NMAX
crt = [0] * NMAX
niv = [[0] * NMAX for _ in range(2)]
G = [[] for _ in range(NMAX)]

#Functions
def Read():
    with open('input.in', 'r') as fin:
        global n, m
        (n, m) = (int(x) for x in fin.readline().split())
        for i in range(0, m):
            (x, y) = (int(x) for x in fin.readline().split())
            G[x].append(y)
            di[y] += 1

def Leveling():

    lg = [0] * 2
    icrt = 0; iurm = 1;
    nr = 0;
    for i in range(1, n+1):
        if (di[i] == 0):
            niv[0][lg[0]] = i
            lg[0] += 1
    while (nr < n):
        for i in range(lg[icrt]):

            fout.write(f"{niv[icrt][i]} ");
            di[niv[icrt][i]] = -1

        lg[iurm] = 0

        for i in range(lg[icrt]):
            x = niv[icrt][i]
            for j in range(len(G[x])):
                neighbor = G[x][j]
                di[neighbor] -= 1
                if (di[neighbor] == 0):
                    niv[iurm][lg[iurm]] = neighbor
                    lg[iurm] += 1

        nr += lg[icrt]
        icrt = 1-icrt
        iurm = 1-iurm


#Main
Read()
with open('output.out', 'w') as fout:
    Leveling()

