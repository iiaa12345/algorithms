def bfs(g, c):
    v = []
    q = [c]
    while len(q) > 0:
        c = q.pop()
        if c not in v:
            print(c + 1)
            v.append(c)
            for i in range(len(g[c])):
                if i not in v and g[c][i] > 0 and i not in q:
                    q.insert(0, i)


g = [[0,  10, 5,  0,  0,  0],
     [10, 0,  2,  5,  2,  0],
     [5,  2,  0,  0,  0,  6],
     [0,  5,  0,  0,  0,  0],
     [0,  2,  0,  0,  0,  4],
     [0,  0,  6,  0,  4,  0]]

bfs(g, 0)
