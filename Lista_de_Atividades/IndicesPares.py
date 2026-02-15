N = int(input())
valores = list(map(int, input().split()))
elementos_indices_pares = [valores[i] for i in range(0, N, 2)]
total_pares = sum(1 for v in valores if v % 2 == 0)
if elementos_indices_pares:
    print(" ".join(map(str, elementos_indices_pares)), total_pares)
else:
    print(total_pares)