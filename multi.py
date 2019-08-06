n=int(input())
l=[int(i) for i in range(1,n+1)]
#print(l)
a=[]
for i in range(0,len(l)):
    a.append(n*l[i])
print(*a)
