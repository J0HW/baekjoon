a,b=map(int, input().split())
arr=[]
for i in range(1, a+1):
  arr.append(i)
for j in range(0,b):
  c,d = map(int, input().split())
  arr[c-1:d]= arr[c-1:d][::-1]
print(*arr)