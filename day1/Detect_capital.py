word=str(input())
if word.istitle() == True :
    print("true")
elif all([True if i.islower() else False for i in word ])==True or all([True if i.isupper() else False for i in word ])==True :
    print ("true")
else:
    print("false")