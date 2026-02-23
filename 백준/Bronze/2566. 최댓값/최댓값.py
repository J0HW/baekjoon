arr1 = [list(map(int, input().split())) for _ in range(9)]

max = -1
max_row, max_val = 0, 0

for r, row in enumerate(arr1):
    for c, val in enumerate(row):
        if max < val:
            max = val
            max_val = c+1
            max_row = r+1

print(max)
print(max_row, max_val)