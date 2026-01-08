arr=[]
arr2=[]
score={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
       'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,'F':0.0}

for _ in range(20):
    a=list(input().split())
    if a[2] != 'P':
        arr.append(a[1])
        if a[2] in score.keys():
            arr2.append(score[a[2]])
        
arr_int = list(map(float, arr))
arr2_int = list(map(float, arr2))
sum=0
sum2=0
for i in arr_int:
    sum += i
for i in range(0,len(arr2_int)):
    sum2 += arr_int[i]*arr2_int[i]

print(sum2/sum)