import sys

def resolver():
    # Lê todos os dados da entrada de uma vez e separa por espaços/quebras de linha [cite: 57, 58, 59]
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    
    while True:
        try:
            # Lê a dimensão N da cidade (N x N quadras) [cite: 58]
            n = int(next(it))
            
            # Reconstrói a malha de esquinas (N+1 x N+1) [cite: 59]
            esquinas = []
            for _ in range(n + 1):
                linha = [int(next(it)) for _ in range(n + 1)]
                esquinas.append(linha)
            
            # Processa cada quadra da cidade [cite: 56, 62]
            for i in range(n):
                resultado_linha = []
                for j in range(n):
                    # As quatro esquinas de uma quadra (i, j) são:
                    # (i, j), (i, j+1), (i+1, j), (i+1, j+1)
                    soma_cameras = (esquinas[i][j] + 
                                    esquinas[i][j+1] + 
                                    esquinas[i+1][j] + 
                                    esquinas[i+1][j+1])
                    
                    # Verifica critério de segurança (mínimo 2 câmeras) [cite: 54]
                    if soma_cameras >= 2:
                        resultado_linha.append('S')
                    else:
                        resultado_linha.append('U')
                
                # Imprime a linha de quadras sem espaços [cite: 62, 63]
                print("".join(resultado_linha))
            
            
        except StopIteration:
            break

if __name__ == "__main__":
    resolver()