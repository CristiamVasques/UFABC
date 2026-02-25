"""
Referência Completa de Python: Tipos de Variáveis e Funções Integradas
Autor: Manus AI
Data: 2026
"""

def demonstrar_python():
    print("--- 1. TIPOS DE VARIÁVEIS (DATA TYPES) ---")
    
    # Numéricos
    inteiro = 42                # int
    ponto_flutuante = 3.1415    # float
    complexo = 3 + 4j           # complex
    booleano = True             # bool (subtipo de int)
    
    # Sequências
    texto = "Olá, Python!"      # str (imutável)
    lista = [1, 2, "três", 4.0] # list (mutável)
    tupla = (10, 20, 30)        # tuple (imutável)
    intervalo = range(0, 10, 2) # range
    
    # Conjuntos (Sets)
    conjunto = {1, 2, 3, 3}     # set (elementos únicos, não ordenados)
    conjunto_imutavel = frozenset([4, 5, 6]) # frozenset
    
    # Mapeamentos
    dicionario = {"chave": "valor", "id": 123} # dict
    
    # Binários
    bytes_dados = b"Hello"      # bytes
    byte_array = bytearray(5)   # bytearray
    memoria = memoryview(bytes_dados) # memoryview
    
    # Especial
    nulo = None                 # NoneType

    # Exibição dos tipos
    tipos = [inteiro, ponto_flutuante, complexo, booleano, texto, lista, tupla, 
             intervalo, conjunto, conjunto_imutavel, dicionario, bytes_dados, 
             byte_array, memoria, nulo]
    
    for t in tipos:
        print(f"Valor: {str(t)[:30]:<30} | Tipo: {type(t)}")

    print("\n--- 2. FUNÇÕES INTEGRADAS (BUILT-IN FUNCTIONS) ---")
    
    # Matemáticas
    print(f"abs(-5): {abs(-5)}")
    print(f"pow(2, 3): {pow(2, 3)}")
    print(f"round(3.567, 2): {round(3.567, 2)}")
    print(f"divmod(10, 3): {divmod(10, 3)}") # (quociente, resto)
    print(f"max/min: {max(lista[0:2])}, {min(lista[0:2])}")
    print(f"sum([1, 2, 3]): {sum([1, 2, 3])}")

    # Conversão de Tipos
    print(f"int('10'): {int('10')}")
    print(f"float(10): {float(10)}")
    print(f"str(100): {str(100)}")
    print(f"list((1, 2)): {list((1, 2))}")
    print(f"bin(10): {bin(10)}")
    print(f"hex(255): {hex(255)}")
    print(f"chr(65): {chr(65)}") # 'A'
    print(f"ord('A'): {ord('A')}") # 65

    # Manipulação de Sequências/Iteráveis
    print(f"len('Python'): {len('Python')}")
    print(f"sorted([3, 1, 2]): {sorted([3, 1, 2])}")
    
    # enumerate() e zip()
    for i, v in enumerate(['a', 'b']):
        print(f"Enumerate {i}: {v}")
    
    pares = list(zip([1, 2], ['um', 'dois']))
    print(f"zip(): {pares}")

    # Funcionais
    numeros = [1, 2, 3, 4]
    dobro = list(map(lambda x: x * 2, numeros))
    pares_filtrados = list(filter(lambda x: x % 2 == 0, numeros))
    print(f"map (dobro): {dobro}")
    print(f"filter (pares): {pares_filtrados}")

    # Inspeção e Ajuda
    print(f"hasattr(texto, 'upper'): {hasattr(texto, 'upper')}")
    print(f"isinstance(inteiro, int): {isinstance(inteiro, int)}")
    print(f"id(inteiro): {id(inteiro)}") # Endereço de memória
    # help(print) # Comentado para não travar a saída

    print("\n--- 3. ESTRUTURAS DE CONTROLE E FUNÇÕES PERSONALIZADAS ---")
    
    # Função com argumentos padrão, arbitrários (*args) e nomeados (**kwargs)
    def funcao_exemplo(padrão="valor", *args, **kwargs):
        """Docstring da função: explica o que ela faz."""
        return f"Args: {args}, Kwargs: {kwargs}"

    print(funcao_exemplo(1, 2, 3, nome="Manus", acao="ajudar"))

    # Geradores (Generators)
    def gerador_simples():
        yield "Primeiro"
        yield "Segundo"
    
    gen = gerador_simples()
    print(f"Generator: {next(gen)}, {next(gen)}")

    # Tratamento de Erros
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro: Divisão por zero capturada!")
    finally:
        print("Bloco 'finally' executado.")

if __name__ == "__main__":
    demonstrar_python()