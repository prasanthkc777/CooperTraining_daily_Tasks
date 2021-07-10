def summ(nn):
    val1 = str(nn)
    listt = list(map(int, val1.strip()))
    return (sum(listt))



value=int(input())
cm=summ(value)
for i in range(value-1,10,-1):
    if(summ(i) > cm):
        print(i)
        break
    else:
        if(i==11):
            print(value)
            break