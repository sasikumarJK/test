a,b=map(int,input().split())
g=[]
for i in range(max(a,b),0,-1):
    if a%i ==0 and b%i ==0:
        g.append(1)
        if len(g)==1:
            print(*g)
            
            
    
