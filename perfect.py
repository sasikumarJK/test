s=int(input())
sum=0
for i in range(1,s):
    if s%i ==0:
        sum +=i
if sum ==s:
    print('perfect number')
else:
    print('not perfect')
    
