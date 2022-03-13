def st (s):
    if s==1:
        return 1
    else:
        return (s*st(s-1))
N=int(input())
sum=0
n=N
while n>0:
    s=n%10
    fact=st(s)
    sum += fact
    n //=10
if sum == N:
    print('strong number')
else:
    print('not strong')
    
