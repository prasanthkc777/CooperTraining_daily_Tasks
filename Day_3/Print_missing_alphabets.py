import string 
myinput=input()
alp=""
for i in string.ascii_lowercase:
    if i not in myinput:
        alp+=i
print(alp)