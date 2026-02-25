while True:
    entrada = input().split()
    M = int(entrada[0])
    
    if M == 0:
        break
    
    N = int(entrada[1])
    moedas = list(map(int, input().split()))
    
    # Inicializa dp
    dp = [M + 1] * (M + 1)
    dp[0] = 0
    
    # Programação Dinâmica
    for moeda in moedas:
        for valor in range(moeda, M + 1):
            if dp[valor - moeda] + 1 < dp[valor]:
                dp[valor] = dp[valor - moeda] + 1
    
    if dp[M] == M + 1:
        print("impossivel")
    else:
        print(dp[M])