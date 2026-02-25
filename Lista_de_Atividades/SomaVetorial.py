while True:
    N = int(input())
    
    if N == 0:
        break
    
    # Lê os vetores
    v = list(map(float, input().split()))
    u = list(map(float, input().split()))
    
    # Soma vetorial
    w = []
    for i in range(N):
        soma = v[i] + u[i]
        w.append(f"{soma:.2f}")
    
    # Imprime o resultado formatado
    print(" ".join(w))
