s=input()
c=0
for i in range(0,len(s)):
    if (s[i].isdigit() or s[i]=='.'):
        c+=1
if c==len(s):
    print("Yes")
else:
    print("No")
