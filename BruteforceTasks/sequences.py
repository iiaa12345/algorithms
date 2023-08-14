n = int(input('n = '))
m = int(input('m = '))
a = [1] * n
i = n - 1

while True:
    print(a)
    i = n - 1
    while i >= 0:
        if a[i] == m:
            a[i] = 1
            i -= 1
        else:
            break
    if i == -1:
        break
    a[i] += 1
