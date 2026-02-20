# Lógica de leitura robusta para capturar todos os dados da entrada
# sem saber exatamente quantas linhas o juiz enviará.
todos_os_dados = []
while True:
    try:
        linha = input().split()
        if not linha:
            break
        for item in linha:
            todos_os_dados.append(int(item))
    except EOFError:
        break

# Processamento apenas se houver dados lidos
if todos_os_dados:
    # N: total, C: carimbadas, M: compradas
    n = todos_os_dados[0]
    c_qtd = todos_os_dados[1]
    m_qtd = todos_os_dados[2]

    # Identifica a lista de figurinhas carimbadas
    # Elas começam no índice 3 e vão até 3 + c_qtd
    carimbadas = todos_os_dados[3:3 + c_qtd]

    # Identifica a lista de figurinhas compradas
    # Elas começam após a lista de carimbadas
    compradas = todos_os_dados[3 + c_qtd:3 + c_qtd + m_qtd]

    # Contador para figurinhas carimbadas que faltam
    faltam = 0

    # Para cada figurinha carimbada, verifica se ela não foi comprada
    for rara in carimbadas:
        ja_possui = False
        
        # Busca manual para verificar presença (sem usar o operador 'in' para ser mais explícito)
        for comp in compradas:
            if rara == comp:
                ja_possui = True
                break
        
        if not ja_possui:
            faltam += 1

    # Saída do número de figurinhas que faltam seguida de salto de linha
    print(faltam)