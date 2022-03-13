n=int(input())
a=[]
sum2=0
for i in range(n+1):
    for j in str(i):
        sum1=int(j)**len(str(i))
        sum2 += sum1
    if sum2==i:
        a.append(i)

print(*a)
