string=str(input())
s=string.replace("#"," ")
li=list(s)
co=0
a=li.index(" ")
for i in range(len(li)):
    if(li[i]==" "):
        if(co<2):
            li[i]="."
            co=co+1
        else:
            li[i]="/"
strs = ''
for ele in li:
    strs += ele
print("https://"+strs+"/")