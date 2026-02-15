"""def calcular_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        proximo = fib[i-1] + fib[i-2]
        fib.append(proximo)
    return fib[n]

print(calcular_fibonacci(10))"""

"""def calcular_fibonacci(n):
    # Definimos os dois primeiros termos
    fib = [0, 1]
    
    # Se o usuário pedir 0 ou 1, retornamos direto do vetor inicial
    if n <= 1:
        return fib[n]
        
    # O laço calcula os próximos termos até chegar em n
    for i in range(2, n + 1):
        proximo = fib[i-1] + fib[i-2]
        fib.append(proximo)
    
    return fib[n]

# Solicita a entrada do usuário e converte para inteiro
#numero = int(input("Digite o termo de Fibonacci que deseja calcular: "))
numero = int(input())

# Chama a função e imprime o resultado
#print(f"O termo {numero} da sequência de Fibonacci é: {calcular_fibonacci(numero)}")
print(f"FIB[{numero}] = ",calcular_fibonacci(numero))"""

def calcular_lista_fibonacci(limite):
    fib = [0, 1]
    for i in range(2, limite + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Pré-calculamos até o máximo permitido (60) para ganhar performance
lista_fib = calcular_lista_fibonacci(60)

# 1. Lê a quantidade de casos de teste (T)
try:
    t_casos = int(input())

    # 2. Loop para processar cada um dos T casos
    for _ in range(t_casos):
        n = int(input())
        
        # 3. Imprime no formato solicitado: FIB[N] = X
        # Note a vírgula separando o texto do valor da lista
        print(f"Fib({n}) = {lista_fib[n]}")

except EOFError:
    pass

"""# 1. Pré-calculamos a sequência de Fibonacci até o 60
fib = [0] * 61
fib[0] = 0
fib[1] = 1
for i in range(2, 61):
    fib[i] = fib[i-1] + fib[i-2]

# 2. Lemos a quantidade de casos de teste (T)
try:
    t_casos = int(input())
    casos_n = []

    # 3. Primeiro, capturamos TODAS as entradas de N
    for _ in range(t_casos):
        n = int(input())
        casos_n.append(n)

    # 4. Somente agora, exibimos TODAS as saídas
    for n in casos_n:
        print(f"Fib({n}) = {fib[n]}")

except EOFError:
    pass"""