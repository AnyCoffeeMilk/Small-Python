n = input().split(",")
t = ['一','二','三','四','五','六','七','八','九']

for i in n:
    ans = ""
    for j in range(int(i)):
        ans += "*"
    for j in range(int(i)):
        ans += t[int(i)-1]
    for j in range(int(i)):
        ans += "*"
    print(ans)
    
        