expressao = input().strip()
referencia = 0
correto = True
for char in expressao:
    if char == '(':
        referencia += 1
    elif char == ')':
        referencia -= 1
        # Se fechar sem ter aberto, já está incorreto
        if referencia < 0:
            correto = False
            break
if correto and referencia == 0:
    print("correct")
else:
    print("incorrect")