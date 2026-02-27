arr1 = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr1[i][j] = 1

cnt = 0
for row in arr1:
    cnt+=row.count(1)

print(cnt)