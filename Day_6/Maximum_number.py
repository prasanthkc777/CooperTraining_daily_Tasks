n, d = map(int, input().split())

score = 0

skip = 0

questions = list(map(int, input().split()))

for i in questions:

    if i <= d:

        score += 1

    else:

        skip+=1

    if skip==2:

        break

print(score)
