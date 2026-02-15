N = int(input())
valores = list(map(int, input().split()))
pares = [v for v in valores if v % 2 == 0]
if pares:
    print(" ".join(map(str, pares)), len(pares))
else:
    print(0)