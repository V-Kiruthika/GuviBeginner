l=input()
n=list(l)
c=0
for i in range(0,len(n)):
    if (n[i].isalpha() or n[i].isdigit() or (ord(n[i])>=21 and ord(n[i])<=47)):
        c+=1
print(c)
