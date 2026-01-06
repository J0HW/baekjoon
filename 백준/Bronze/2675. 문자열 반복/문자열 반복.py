a=int(input())
for i in range(0, a):
  n, s = input().split()
  n = int(n)
  s = list(s)
  for j in range(len(s)):
    print(s[j]*n,end='')
  print()