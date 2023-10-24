n = input().split(" ")
t = ["a","b","c","d","e","f","g","h","i","j"]

ans = []
for j, i in enumerate(n):
    if i in t:
        ans.append(i)
        continue
    try:
        if int(i) >= 0 and int(i) <= 9:
            ans.append(i)
            continue
        elif int(i) % 11 == 0 and int(i) >= 0:
            ans.append(i)
            continue
    except:
        continue
    
    
if ans == []:
    print("沒有合適的符號")
else:
    print(",".join(ans))