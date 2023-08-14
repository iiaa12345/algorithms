def qsort(a):
    if len(a) <= 1:
        return a
    else:
        b = []
        c = []
        mid = len(a) // 2
        for i in range(len(a)):
            if a[i] < a[mid]:
                b.append(a[i])
            if a[i] > a[mid]:
                c.append(a[i])
        return qsort(b) + [a[mid]] + qsort(c)

a = list(map(int, input().split()))

print(qsort(a))
