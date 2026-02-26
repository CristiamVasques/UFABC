import sys

# Leitura ultra-rápida
input_data = sys.stdin.read().split()

it = iter(input_data)

while True:
    try:
        m = int(next(it))
        n = int(next(it))
        if m == 0: break
        
        moedas = [int(next(it)) for _ in range(n)]
        
        # trocos_alcançaveis é um número onde o bit 'i' ligado 
        # significa que conseguimos formar o valor 'i'.
        # Começamos com o bit 0 ligado (valor 0 com 0 moedas).
        trocos_alcancaveis = 1
        objetivo = 1 << m
        
        # Se o troco já for 0 (caso bizarro, mas possível)
        if m == 0:
          continue

        moedas_usadas = 0
        possivel = False
        
        # Enquanto ainda houver trocos novos para tentar
        # e não passarmos do limite lógico de moedas
        for qtd in range(1, m + 1):
            proximos_trocos = 0
            for moeda in moedas:
                # Desloca todos os trocos atuais pelo valor da moeda
                proximos_trocos |= (trocos_alcancaveis << moeda)
            
            # Mantém apenas os bits que nos interessam (até o troco M)
            # Isso evita que o número cresça infinitamente
            trocos_alcancaveis = proximos_trocos & ((1 << (m + 1)) - 1)
            
            # Se o bit do nosso objetivo estiver ligado, achamos!
            if (trocos_alcancaveis & objetivo):
                print(f"{qtd}")
                possivel = True
                break
            
            # Se após tentar todas as moedas não sobrou nenhum bit novo, 
            # significa que não dá para avançar mais.
            if trocos_alcancaveis == 0:
                break

        if not possivel:
            print("impossivel")
            
    except StopIteration:
        break