a, b = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(a)]
arr2 = [list(map(int, input().split())) for _ in range(a)]
result = []

for i in range(a):
    row = []
    for j in range(b):
        row.append(arr1[i][j] +  arr2[i][j])
    result.append(row)

for row in result:
    print(*row)