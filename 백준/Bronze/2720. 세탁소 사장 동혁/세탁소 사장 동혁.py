t = int(input())
arr = []
for _ in range(0, t):
    c = int(input())
    arr.append(c)

for i in arr:
    q = i // 25
    d = i % 25
    n = d % 10
    if n < 5:
        p = n
        n = 0
    else:
        p = n % 5
        n = n // 5
    d = d // 10
    print(q,d,n,p)