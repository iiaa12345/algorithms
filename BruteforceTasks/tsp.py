def tsp(g, a):
    s = 0
    for i in range(len(a) - 1):
        if g[a[i]][a[i + 1]] > 0:
            s += g[a[i]][a[i + 1]]
        else:
            return
    if g[a[i + 1]][a[0]] > 0:
        return s + g[a[i + 1]][a[0]]


g = [[0, 2, 0, 4, 0],
     [2, 0, 0, 0, 3],
     [0, 0, 0, 2, 2],
     [4, 0, 2, 0, 5],
     [0, 3, 2, 5, 0]]

n = len(g)
a = [i for i in range(n)]
min_dist = 100500
min_a = None

while True:
    dist = tsp(g, a)
    if dist != None:
        if min_dist > dist:
            min_dist = dist
            min_a = a[:]

    i = n - 2
    while a[i] >= a[i + 1]:
        i -= 1
        if i < 0:
            break

    if i < 0:
         break

    min_j = None
    for j in range(i + 1, n):
        if min_j == None and a[j] > a[i]:
            min_j = j
        if min_j != None and a[j] < a[min_j] and a[j] > a[i]:
            min_j = j

    a[i], a[min_j] = a[min_j], a[i]

    k = i + 1
    l = n - 1
    while k < l:
        a[k], a[l] = a[l], a[k]
        k += 1
        l -= 1

print(min_dist)
print(min_a)
