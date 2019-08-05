n=input()
x=["a","A","E","I","O","U","e","i","o","u"]
if not(n.isalpha()):
    print("invalid")
elif n in x:
    print("Vowel")
else:
    print("Consonant")
