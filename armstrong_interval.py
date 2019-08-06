def arm(m):
    s=0
    while m>0:
        d=m%10
        s+=d**3
        m=m//10
    return s
n,e=map(int,input().split())
l=[]
for i in range(n+1,e):
    if i==arm(i):
        l.append(i)
print(*l)
