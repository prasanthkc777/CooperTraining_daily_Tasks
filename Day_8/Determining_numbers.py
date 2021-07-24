from collections import Counter
x = int(input())
s1 = list((map(int, input().split())))
f=[str(i) for i in s1]
a = []

for i in f:

    counter = Counter(f)
    out = counter[i]
    if (out == 1):
        a.append(int(i))

final0 = ""
final1 = sorted(a)

for j in final1:
    final0 += str(j) + " "
print(final0)
