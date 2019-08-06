def arm(m):
    s=0
    while m>0:
        d=m%10
        s+=d*d*d
        m=m//10
    return s
n=int(input())
f=arm(n)
if (f==n):
    print("yes")
else:
    print("no")
