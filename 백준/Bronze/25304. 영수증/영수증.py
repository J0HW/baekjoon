a = int(input())
b = int(input())
sum = 0
for i in range(0,b):
  c,d = map(int, input().split())
  sum = sum + c*d

if a == sum:
  print('Yes')
else:
  print('No ')