inp = list(map(int,input().split(':')))
inp2 = int(input())
for _ in range(inp2):
    t = list(map(int,input().split(':')))
    x = (inp[0]-t[0])*3600 + (inp[1]-t[1])*60 + (inp[2]-t[2])
    if(x==0):
        print("now")
    elif(x==1):
        print("1 second ago")
    elif(x>=2 and x<60):
        print(x,"seconds ago")
    elif(x>=60 and x<120):
        print("1 minute ago")
    elif(x>=120 and x<3600):
        x = int(x/60)
        print(x,"minutes ago")
    elif(x>=3600 and x<7200):
        print("1 hour ago")
    else:
        x = int(x/3600)
        print(x,"hours ago")
