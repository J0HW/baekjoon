arr =[]
for i in range(1, 29):
  arr.append(int(input()))
arr.sort()

for i in range(1, 31):
  if i not in arr:
    print(i)