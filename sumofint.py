n,k = map(int,input().split())
n=list(map(int,input().split()))
#print(n)
d=0
for i in range(0,k):
    d+=n[i]
print(d)
