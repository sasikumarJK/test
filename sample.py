a,b=map(int,input().split())
list1=[]
for i in range(1,b+1):
    fact1=a*i
    for j in range(1,a+1):
        fact2=b*j
        if fact1==fact2:
            list1.append(fact1)
            if len(list1)==1:
                print(*list1)
