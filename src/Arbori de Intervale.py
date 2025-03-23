#infoarena Arbori de intervale

#Constant variables
NMAX = 100005

#Initialisation
lineIndex = -1
aint = [0] * NMAX * 4
v = [0] * NMAX

#Functions
def build(nod, st, dr):
    if st == dr:
        aint[nod] = v[st]
        return

    mij = (st+dr) // 2
    build(nod*2, st, mij)
    build(nod*2+1, mij+1, dr)

    aint[nod] = max(aint[nod*2], aint[nod*2+1])


def query(nod, st, dr, a, b):
    if a <= st and dr <= b:
        return aint[nod]

    ansl = 0; ansr = 0
    mij = (st+dr) // 2
    if a <= mij:
        ansl = query(nod*2, st, mij, a, b)
    if mij+1 <= b:
        ansr = query(nod*2+1, mij+1, dr, a, b)

    return max(ansl, ansr)

def update(nod, st, dr, pos, val):
    if st == dr:
        aint[nod] = val
        return

    mij = (st+dr) // 2
    if pos <= mij:
        update(nod*2, st, mij, pos, val)
    else:
        update(nod*2+1, mij+1, dr, pos, val)

    aint[nod] = max(aint[nod*2], aint[nod*2+1])


#Read Values
with open('../.venv/prim.in', 'r') as fin:
    line = fin.readlines()
fout = open('../.venv/prim.out', 'w')

lineIndex += 1
n, m = (int(x) for x in line[lineIndex].split())
lineIndex += 1
v = [0] + [int(x) for x in line[lineIndex].split()]

build(1, 1, n)

for i in range(1, m+1):
    lineIndex += 1
    op, a, b = (int(x) for x in line[lineIndex].split())
    if op == 0:
        fout.write(str(query(1, 1, n, a, b)) + '\n')
    else:
        update(1, 1, n, a, b)
