def myfun(myinp):
    if len(myinp) == 1:
        return myinp[0].upper()
    emp = []
    emp.append(myinp[0].upper())
    prev = None
    count = None
    for i in range(1,len(myinp)):
        if myinp[i] in 'aeiou':
            if not prev or (prev!=myinp[i] and prev in 'aeiou'):
                emp.append(myinp[i])
                prev = myinp[i]
            elif prev in 'bcdfghjklmnpqrstvwxyz':
                emp.append(str(count))
                emp.append(myinp[i])
                prev = myinp[i]
            else:
                pass
        else:
           
            if not prev:
                prev = myinp[i]
                count = 1
            elif prev in 'aeiou':
                prev = myinp[i]
                count = 1
            else:
                prev = myinp[i]
                count+=1
    if myinp[i] in 'bcdfghjklmnpqrstvwxyz':
        emp.append(str(count))
    return ''.join(emp)
 
for z in range(int(input())):
  inp = input()
  myinp = input()
    
    
    
  print(myfun(myinp))
