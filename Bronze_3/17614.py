n = int(input())

cnt = 0
for i in range(1, n+1):
    n = str(i)

    for j in n:
        if j in "369":
            cnt += 1

print(cnt)
