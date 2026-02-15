p1 = input().strip()
N = int(input())
encontrou = False
for _ in range(N):
    palavra = input().strip()
    if palavra == p1[::-1]:
        encontrou = True
if encontrou:
    print("sim")
else:
    print("nao")