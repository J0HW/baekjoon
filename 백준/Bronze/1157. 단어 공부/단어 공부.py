a = input().upper()
a_list = list(set(a))
c=[]
for i in a_list:
    cnt = a.count(i)
    c.append(cnt)
if c.count(max(c)) > 1:
    print('?')
else:
    print(a_list[c.index(max(c))])