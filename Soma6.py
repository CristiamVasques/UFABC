soma = 0
numeros = input().split()
i = 0
while(numeros[i] != "0"):
      soma = soma + int(numeros[i])
      i = i + 1

print(soma)