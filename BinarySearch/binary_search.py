a = list(map(int, input().split()))
k = int(input())
st = 0
en = len(a) - 1
fl = False

while en > st:
    mid = (st + en) // 2
    if a[mid] == k:
        fl = True
        break
    elif a[mid] < k:
        st = mid + 1
    else:
        en = mid - 1

if fl:
    print("YES")
else:
    print("NO")
