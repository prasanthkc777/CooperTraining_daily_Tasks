myinp = int(input())
 
myarray = list(map(int, input().split()))
 
stack = []
 
 
 
for i in range(myinp):
 
   if not myarray [i] % 2:
 
       stack.append(myarray [i])
 
       continue
 
   else:
 
       if stack:
 
           while stack:
 
               print(stack.pop(), end=" ")
 
       else:
 
           print(myarray [i], end=" ")
 
           continue
 
       print(myarray [i], end=" ")
 
 
 
if stack:
 
   while stack:
 
       print(stack.pop(), end=" ")
