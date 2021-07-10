import json

inp = input()
n = inp[(inp.index("#") + 1):]
tat = ''.join([i for i in inp[:-2] if (i.isdigit() == 1)])
target = list(tat)
res = []
last = 0
for x in target:
    diff = int(x) - last - 1
    if diff:
        res += ["Push", "Pop"] * diff
    res += ["Push"]
    last = int(x)
r = ",".join([str(i) for i in res])
r1 = r.split(",")
r2 = json.dumps(r1)
r3 = str(r2)
r4 = r3.replace(", ", ",")
print(r4)