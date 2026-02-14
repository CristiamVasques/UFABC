#Recebe um número inteiro ou string e printa na tela

entrada = input()

try:
    N = int(entrada)
except ValueError:
    N = entrada  # mantém como string

print(N)
