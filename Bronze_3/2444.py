num = int(input())

for i in range(1, num+1):
    print(" " * (num - i) + "*" * i + "*" * (i - 1))

print(end="")

for i in range(num-1, 0, -1):
    print(" " * (num - i) + "*" * i + "*" * (i - 1))
