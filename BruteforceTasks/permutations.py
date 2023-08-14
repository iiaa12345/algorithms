n = int(input("n = "))
a = [i + 1 for i in range(n)]

while True:
    print(a)

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
