 s= int(input())
count = 0
heights = [int(i) for i in str(s)]

for p, q in zip(heights, sorted(heights)):
    if p != q:
        count += 1
print(count)

