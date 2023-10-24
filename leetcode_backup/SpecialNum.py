a = int(input())
n = [2, 3, 5]
tmp = 1
ans = [1]
counter = 0
while counter < a:
    for i in n:
        if (tmp * i) not in ans:
            ans.append(tmp * i)
            ans.sort()
    for i in ans:
        if tmp < i:
            tmp = i
            counter += 1
            break
print(ans[a - 1])