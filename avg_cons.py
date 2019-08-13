n=int(input())
m=list(map(int,input().split()))
if len(m)==n:
    p=sum(m)//n
    print(p)
