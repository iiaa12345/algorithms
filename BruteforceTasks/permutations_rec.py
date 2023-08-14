def perm(a, k):
    if k == len(a) - 1:
        print(a)
    else:
        for i in range(k + 1, len(a)):
            a[i], a[k] = a[k], a[i]
            perm(a, k + 1)
            a[i], a[k] = a[k], a[i]


n = int(input("n = "))
a = [i + 1 for i in range(n)]

perm(a, 0)
