n=int(input())
c=0
while n!=0:
    r=n%10
    c = c + r
    n //= 10
print(c)
