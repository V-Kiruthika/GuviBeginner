n=input()
c=0
for i in n:
    if not(i.isalpha() or i.isdigit() or ord(i)==32):
        c+=1
print(c)
