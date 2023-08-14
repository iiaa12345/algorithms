def verify(a, ans, k, n):
    i = 0
    t = 0
    m = 1
    while t < n - 1:
        if a[t + 1] - a[i] >= ans:
            m += 1
            i = t
        t += 1
    return k <= m


n, k = map(int, input().split())
a = list(map(int, input().split()))
st = 0
en = max(a) - min(a)

max_ans = en
while en > st:
    mid = (st + en) // 2
    if verify(a, mid, k, n):
        max_ans = mid
        st = mid + 1
    else:
        en = mid - 1

print(max_ans)
