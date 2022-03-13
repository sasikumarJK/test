def fun (a):
    return lambda b: b+a

c=fun(10)
d=c(15)
print(d)

    
