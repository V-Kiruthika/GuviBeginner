n=int(input())
m=list(map(int,input().split()))
m.sort()
#print(*m)
a=(len(m)//2)
if (len(m)%2!=0):
    print(m[a])
else:
    print((m[a]+m[a-1])/2)
