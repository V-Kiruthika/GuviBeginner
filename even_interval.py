s,e=map(int,input().split())
l=[]
for i in range(s+1,e):
    if i%2==0:
        l.append(i)
print(*l)
