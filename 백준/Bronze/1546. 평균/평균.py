n = int(input())
arr = list(map(int, input().split()))
a = []
for i in arr:
  m=max(arr)
for i in range(0,n):
  b = arr[i]/m*100 
  a.append(b)
print(sum(a)/n)