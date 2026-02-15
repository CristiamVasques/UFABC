# Inicialização das variáveis de controle
maior_palavra = ""
palavra_informada = False

try:
    # Loop infinito para ler a entrada padrão
    while True:
        try:
            # Captura a linha de entrada
            linha = input().strip()
            
            # Pula linhas vazias que não contenham palavras
            if not linha:
                continue
            
            palavra_informada = True
            
            # Se o comprimento da nova palavra for maior ou IGUAL,
            # atualizamos para garantir que a última apareça em caso de empate 
            if len(linha) >= len(maior_palavra):
                maior_palavra = linha
                
        except EOFError:
            # Sai do loop quando o fim do arquivo (EOF) é atingido 
            break

    # Verificação final e saída conforme especificado 
    if palavra_informada:
        print(f"A maior palavra informada foi {maior_palavra}")
    else:
        print("Nenhuma palavra foi informada")

except Exception:
    # Tratamento genérico para evitar interrupções inesperadas
    pass