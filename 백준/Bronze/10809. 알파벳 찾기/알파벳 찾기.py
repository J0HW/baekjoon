s= input()
a = []
for i in range(ord('a'), ord('z') + 1): 
  a.append(chr(i))
for i in a:
  if i in s:
    print(s.index(i), end=' ')
  else:
    print(-1, end=' ')