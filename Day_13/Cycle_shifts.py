for cycle in range(0,int(input())):
    s,n,c=input().split()
    s,n=int(s),int(n)
    n_bin=str(bin(s))[2:].zfill(16)
    if(c=='R'):
        binary=n_bin[-n:]+n_bin[:-n]
    else:
        binary=n_bin[n:]+n_bin[:n]
    print(int(binary,2))
