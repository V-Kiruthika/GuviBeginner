n,m=map(str,input().split())
l=[]
k=[]
for i in n:
    l.append(ord(i))
for j in m:
    k.append(ord(j))
'''print(l)
print(k)'''
b=min(len(l),len(k))
#print(b)
for g in range(0,b):
    if l[g]>k[g]:
        print(n)
        break;
    elif k[g]>l[g]:
        print(m)
        break;
    else:
        print(n)
        break;
