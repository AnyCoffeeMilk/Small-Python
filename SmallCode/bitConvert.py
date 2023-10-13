import string
a = int(input())
b = int(input())
d = []
while True:
    d.append(a % b)
    a = int(a / b)
    if a == 0:
        break
e = []
for i in d:
    e.append(str(i))
e.reverse()
f = string.ascii_uppercase[:21]
for j, i in enumerate(e):
    if int(i) >= 10:
        e[j] = f[int(i) - 10]
print("".join(e))