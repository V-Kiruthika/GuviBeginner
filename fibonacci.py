m=int(input())
a,b=1,1
l=[a,b]
for i in range(2,m):
    d=a+b
    l.append(d)
    a=b
    b=d
print(*l)
    
