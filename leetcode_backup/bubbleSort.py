def mppx(datas):
    ans = 0
    length = len(datas)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if datas[j] > datas[j+1]:
                temp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = temp
                ans += 1
    return ans

print(mppx(eval(input())))