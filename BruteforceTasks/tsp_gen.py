import random

INF = 100500
NMAX = 50


def fitness(a):
    s = 0
    for i in range(len(a) - 1):
        if g[a[i]][a[i + 1]] > 0:
            s += g[a[i]][a[i + 1]]
        else:
            return INF
    if g[a[i + 1]][a[0]] > 0:
        return s + g[a[i + 1]][a[0]]
    else:
        return INF


def generate(p, l):
    c = []
    a = [i for i in range(l)]
    while len(c) < p:
        random.shuffle(a)
        c.append(a[:])
    return c


def crossover(c, p, l):
    for i in range(p - 1):
        for j in range(i + 1, p):
            rand = random.randint(1, l - 2)
            a = []
            for k in c[i][:rand]:
                a.append(k)
            for k in c[j][rand:]:
                if k not in a:
                    a.append(k)
            for k in c[j][:rand]:
                if k not in a:
                    a.append(k)
            b = []
            for k in c[j][:rand]:
                b.append(k)
            for k in c[i][rand:]:
                if k not in b:
                    b.append(k)
            for k in c[i][:rand]:
                if k not in b:
                    b.append(k)
            c.append(a)
            c.append(b)
    return c


def mutations(c, mut_prob, l):
    for i in range(len(c)):
        if random.randint(0, 100) <= mut_prob:
            a = random.randint(0, l - 1)
            b = random.randint(0, l - 1)
            c[i][a], c[i][b] = c[i][b], c[i][a]
    return c


def selection(c, p):
    c.sort(key=fitness)
    c = c[:p]
    return c


p = int(input())
mut_prob = int(input())
k = int(input())

l = NMAX
g = []
for i in range(l):
    a = []
    for j in range(l):
        d = random.randint(10, 100)
        if i != j:
            a.append(d)
        else:
            a.append(0)
    g.append(a)

c = generate(p, l)

for i in range(k):
    c = crossover(c, p, l)
    c = mutations(c, mut_prob, l)
    c = selection(c, p)
    if i % 10 == 0:
        print(fitness(c[0]))

print(fitness(c[0]))
