while True:
    a = int(input())
    if a == -1:
        break
    f = 0 
    arr = []
    for i in range(1,a,1):
        if a % i == 0:
            f += i
            arr.append(i)
    if f == a:
        print(a, '=', end=" ")
        print(*arr, sep=" + ")
    else:
        print(a, 'is NOT perfect.')