n = int(input())
cnt = n
for _ in range(n):
    s = input()
    seen=set()
    seen.add(s[0])
    for i in range(0,len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1] in seen:
                cnt-=1
                break
            seen.add(s[i+1])
            
print(cnt)