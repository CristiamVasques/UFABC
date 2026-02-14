#Recebe os números que serão somados, para interromper a digitação de números CTRL+D

Soma = 0

while True:
    try:
        Valor = int(input())
        Soma += Valor
    except EOFError:
        break

print(Soma)