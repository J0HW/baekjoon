n = int(input())
line = 1
max_num = 1
while n > max_num:
    line += 1
    max_num += line
min_num = (max_num - line)+1
chae = n - min_num
if line % 2 == 1:
    a = line - chae
    b = 1 + chae
else:
    a = 1 + chae
    b = line - chae
print(a, '/', b, sep="")