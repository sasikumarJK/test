n=int(input())
cp=n
s=0
for i in range(n):
    r= n %10
    s= s + (r*r*r)
    n //= 10
if s == cp:
    print('armstrong')
else:
    print('not armstrong')
