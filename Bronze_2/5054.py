t = int(input())

for i in range(t):
    n = int(input())
    li = sorted(list(map(int, input().split())))

    print((li[-1] - li[0]) * 2)
