a=input()
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
c=0
for i in range(len(a)):
  for j in b:
    if a[i] in j:
      c += b.index(j)+3
print(c)