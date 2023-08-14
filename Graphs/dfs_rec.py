def dfs(g, c, v):
    print(c + 1)
    v.append(c)
    for i in range(len(g[c])):
        if i not in v and g[c][i] > 0:
            dfs(g, i, v)


g = [[0,  10, 5,  0,  0,  0],
     [10, 0,  2,  5,  2,  0],
     [5,  2,  0,  0,  0,  6],
     [0,  5,  0,  0,  0,  0],
     [0,  2,  0,  0,  0,  4],
     [0,  0,  6,  0,  4,  0]]

dfs(g, 0, [])
