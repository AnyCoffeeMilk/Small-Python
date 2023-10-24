h = input().split(" ")
tmp = 0
ans = 0
down = False

for j, i in enumerate(h):
    if tmp == 0:
        tmp = i
        continue
    if down == True and i > tmp:
        down = False
        tmp = i
        continue
    if tmp > i and j != 1 and down == False:
        ans += 1
        down = True
        tmp = i
        continue
    tmp = i

print(ans)