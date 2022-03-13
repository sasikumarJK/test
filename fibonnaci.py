n=int(input('enter'))
i=0
j=1
t=0
while t < n:
    print(i, end=' ')
    k=i+j
    i=j
    j=k
    t+=1
    
