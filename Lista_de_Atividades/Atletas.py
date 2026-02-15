idades = []
alturas = []
pesos = []
generos = []
qtdMasc = 0
qtdFem = 0
qtdMascAcimaAlt = 0
qtdFemAbaixoPeso = 0
somaAltMasc = 0
somaPesoFem = 0
TAMANHO = 100

for i in range(0, TAMANHO, 1):
    print("Informe a idade do " + str(i+1) + "o. atleta: ", end="")
    idades.append(int(input()))
    print("Informe a altura do " + str(i+1) + "o. atleta: ", end="")
    alturas.append(int(input()))
    print("Informe a peso do " + str(i+1) + "o. atleta: ", end="")
    pesos.append(int(input()))
    print("Informe a genero do " + str(i+1) + "o. atleta: ", end="")
    generos.append(int(input()))

    if(generos[i] == 'M'):
        somaAltMasc = somaAltMasc + alturas[i]
        qtdMasc = qtdMasc + 1
    else:
        somaPesoFem = somaPesoFem + pesos[i]
        qtdFem = qtdFem + 1

for i in range(0, TAMANHO, 1):
    if(qtdMasc != 0 and alturas[i] > (somaAltMasc/qtdMasc) and generos[i] == 'M'):
        qtdMascAcimaAlt = qtdMascAcimaAlt + 1

    if(qtdFem != 0 and pesos[i] < (somaPesoFem/qtdFem) and generos[i] == 'F'):
        qtdFemAbaixoPeso = qtdFemAbaixoPeso + 1

if(qtdMasc != 0):
    print("Ha " + str(qtdMascAcimaAlt) + " atletas homens acima da media da altura dos homens.")
else:
    print("Nao houve entrada de atletas homens.")

if(qtdFem != 0):
    print("Ha " + str(qtdMascAcimaAlt) + " atletas mulheres abaixo da media do peso das mulheres.")
else:
    print("Nao houve entrada de atletas mulheres.")
    