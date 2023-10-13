inp = [int(i) for i in input().split(" ")]

ans = [["*" for _ in range(len(inp))] for _ in range(max(inp))]

for x, y in enumerate(inp):
    for i in range(len(ans)- y):
        ans[i][x] = " "

rt = ''

for q, i in enumerate(ans):
    for p, j in enumerate(i):
        rt += j
        if p != len(i)-1:
            rt += ' '
    if q != len(ans)-1:
        rt += '\n'

print(rt)