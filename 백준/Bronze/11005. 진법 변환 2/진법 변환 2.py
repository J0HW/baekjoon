n, b = map(int, input().split())
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = []
while n > 0:
    nb=n%b
    n=n//b
    arr.append(chars[nb])

arr.reverse()
print("".join(arr))