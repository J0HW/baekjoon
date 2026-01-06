arr =[0]*42
for i in range(0, 10):
  a=(int(input()))
  arr[a%42]=1
print(sum(arr))