def rseq(a, m, n, j):
    if j >= n:
        print(a)
    else:
        for i in range(1, m + 1):
            a[j] = i
            rseq(a, m, n, j + 1)


n = int(input('n = '))
m = int(input('m = '))

a = [1] * n

rseq(a, m, n, 0)
