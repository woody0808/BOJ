num = int(input())

for i in range(num):
    n = int(input())

    cnt = 0
    while n > 0:
        if n % 2 == 1:
            print(cnt, end=" ")

        n //= 2
        cnt += 1
