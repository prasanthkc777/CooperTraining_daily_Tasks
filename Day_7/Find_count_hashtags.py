import re
from collections import  Counter,OrderedDict
my_inp = int(input())
string_ =''
for i in range(my_inp):
    string_+=str(input())
    string_+=" "
my_list = list(string_.split(" "))

output=[]
for i in my_list:

    test = re.search(r"\#\w+",i)
    if test:
        output.append(i)
class OrderedCounter(Counter,OrderedDict):
    pass
[print(z[0]) for z in OrderedCounter (sorted(output)).most_common(5)]
