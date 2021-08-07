my_inp = int(input())
for _ in range(my_inp):
    s = int(input())
    c = map(int, input().split())
    calc = sum(1 if ele % 2 == 0 else 0 for ele in c)
    print(min(calc, s - calc))
