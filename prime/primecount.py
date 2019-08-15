def prime(n):
    c=0
    for j in range(2,n):
        if n%j==0:
            c+=1
    if c==0:
        a=1
    else:
        a=0
    return a
s,e=map(int,input().split())
d=0
for i in range(s,e+1):
    if prime(i)==1:
        d+=1
print(d)
