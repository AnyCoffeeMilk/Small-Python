h = input().split(" ")
a, b, x, y = int(h[0]), int(h[1]), int(h[2]), int(h[3])
ps = "{:.100f}".format(float(a/b))
ans = str(ps).split(".")[1]
if len(ans) < y:
    for i in range(y):
        ans += "0"
print(ans[x-1:y])