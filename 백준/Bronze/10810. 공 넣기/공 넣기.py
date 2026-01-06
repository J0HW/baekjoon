a,b=map(int, input().split())
arr = []
for i in range(a):
  arr.append(0)

for j in range(0,b):
  c,d,e=map(int, input().split())
  for k in range(c-1, d):
    arr[k] = e

print(*arr)