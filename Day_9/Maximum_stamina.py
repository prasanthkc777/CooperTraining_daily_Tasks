
myinp=int(input())
arr=list(map(int,input().split()))
myarr=[]
for i in range(myinp-1):
    checkmax=arr[i]
    eval_out=str(arr[i])
    for j in range(i+1,myinp):
        if arr[j]>checkmax:
            checkmax=arr[j]
            eval_out+='^'+str(arr[j])
    
    myarr.append(eval(eval_out))


myarr.append(arr[-1])

print(max(myarr))
