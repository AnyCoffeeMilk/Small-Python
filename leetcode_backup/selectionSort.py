a = eval(input())
ans = 0
for i in range(len(a) - 1):
    i_min = i
    for j in range(i + 1, len(a)):
        if a[j] < a[i_min]:
            i_min = j
    if i != i_min:
        a[i], a[i_min] = a[i_min], a[i]
        ans += 1
print(ans)