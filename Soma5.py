#Receba uma sequência indefinida de números inteiros positivos e realiza a soma desses valores.

soma = 0
num =int(input())
while(num != 0):
    soma = soma + num
    num = int(input())

print(soma)
