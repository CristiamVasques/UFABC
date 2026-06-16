import sys
import subprocess

# --- Verificação de Ambiente ---
# Garante a portabilidade do script entre diferentes ambientes de desenvolvimento
try:
    import pandas as pd
    print("Ambiente OK: Biblioteca 'pandas' já está instalada.")
except ImportError:
    print("Pandas não encontrado. Instalando automaticamente...")
    # Executa o gerenciador pip utilizando o mesmo interpretador Python em execução
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd
    print("Pandas instalado com sucesso!\n")

import random
from datetime import datetime, timedelta

class GeradorInstanciasNOC:
    """
    Gerador de instâncias sintéticas para simulação e otimização de escalas
    e fluxos de trabalho em Centros de Operações de Rede (NOC).
    """
    def __init__(self, seed=42):
        # Definição de semente pseudoaleatória para garantir a replicabilidade científica dos testes
        random.seed(seed)
        
        # Parâmetros operacionais do domínio de infraestrutura de TI
        self.niveis_criticidade = ['Baixa', 'Média', 'Alta', 'Crítica']
        self.competencias_disponiveis = ['Cloud', 'Networks', 'Operating Systems', 'Cybersecurity', 'DevOps']
        
    def gerar_analistas(self, qtd_analistas=10):
        """
        Gera o cadastro de analistas e sua respectiva matriz de competências técnicas.
        """
        analistas = []
        for i in range(1, qtd_analistas + 1):
            # Define uma quantidade variável de especialidades por profissional
            qtd_comp = random.randint(1, 3)
            competencias = random.sample(self.competencias_disponiveis, qtd_comp)
            
            # Classificação de nível com base no escopo de competências
            if qtd_comp == 1:
                nivel = 'N1'
            elif qtd_comp == 2:
                nivel = 'N2'
            else:
                nivel = 'N3'
                
            analistas.append({
                'id_analista': f'AN_{i:02d}',
                'nome': f'Analista {i}',
                'nivel': nivel,
                'competencias': competencias,
                'max_horas_semanais': 44  # Limite de jornada padrão da legislação vigente
            })
        return pd.DataFrame(analistas)

    def gerar_estrutura_turnos(self, data_inicio, dias=7):
        """
        Gera a grade horária de turnos necessária para manter a cobertura de uma operação 24x7.
        """
        turnos = []
        data_atual = datetime.strptime(data_inicio, "%Y-%m-%d")
        
        # Estrutura padrão de passagens de turno em monitoramento contínuo
        horarios_turnos = [
            {'nome': 'T1_Matutino', 'inicio': '05:40', 'fim': '15:28'},
            {'nome': 'T2_Comercial', 'inicio': '08:00', 'fim': '17:48'},
            {'nome': 'T1_Vespertino', 'inicio': '12:12', 'fim': '22:00'},
            {'nome': 'T3_Noite', 'inicio': '21:40', 'fim': '06:00'}
        ]
        
        for d in range(dias):
            data_str = data_atual.strftime("%Y-%m-%d")
            for h in horarios_turnos:
                turnos.append({
                    'id_turno': f"TURNO_{data_str}_{h['nome']}",
                    'data': data_str,
                    'tipo_turno': h['nome'],
                    'hora_inicio': h['inicio'],
                    'hora_fim': h['fim'],
                    # Dimensionamento de capacidade mínima: contingência reduzida na madrugada
                    'min_analistas_requeridos': 2 if h['nome'] == 'T1_Madrugada' else 3
                })
            data_atual += timedelta(days=1)
            
        return pd.DataFrame(turnos)

    def gerar_volumetria_alertas(self, data_inicio, dias=7, estresse=False):
        """
        Gera o fluxo de incidentes e alertas que entram na fila do NOC.
        O parâmetro 'estresse' simula cenários de crise ou degradação severa da infraestrutura.
        """
        alertas = []
        data_atual = datetime.strptime(data_inicio, "%Y-%m-%d")
        id_alerta = 1
        
        # Configuração da taxa de chegada de eventos por hora (Cenário de Teste vs. Controle)
        media_alertas_por_hora = 15 if estresse else 4
        
        for d in range(dias):
            for hora in range(24):
                # Simulação de flutuação estatística de chamados na hora
                qtd_alertas_na_hora = random.randint(int(media_alertas_por_hora * 0.5), int(media_alertas_por_hora * 1.5))
                
                for _ in range(qtd_alertas_na_hora):
                    criticidade = random.choices(self.niveis_criticidade, weights=[0.5, 0.3, 0.15, 0.05])[0]
                    competencia_requerida = random.choice(self.competencias_disponiveis)
                    
                    # Em cenários de estresse, a probabilidade de incidentes críticos escala
                    if estresse and random.random() > 0.7:
                        criticidade = 'Crítica'
                    
                    momento_alerta = data_atual + timedelta(hours=hora, minutes=random.randint(0, 59))
                    
                    alertas.append({
                        'id_alerta': f'ALE_{id_alerta:05d}',
                        'timestamp': momento_alerta.strftime("%Y-%m-%d %H:%M:%S"),
                        'criticidade': criticidade,
                        
                        # REFERÊNCIA AO ALGORITMO GULOSO:
                        # Esta chave mapeia o critério técnico essencial que a heurística gulosa de 
                        # ordenação utilizará para casar a demanda imediata com o perfil do analista.
                        'heuristica_gulosa_prioridade': competencia_requerida,
                        
                        'tempo_estimado_solucao_min': random.choice([15, 30, 45, 60, 120])
                    })
                    id_alerta += 1
            data_atual += timedelta(days=1)
            
        return pd.DataFrame(alertas)

    def gerar_instancia_completa(self, data_inicio, dias=7, qtd_analistas=10, estresse=False):
        """
        Consolida a geração dos subconjuntos de dados em um dicionário estruturado.
        """
        df_analistas = self.gerar_analistas(qtd_analistas)
        df_turnos = self.gerar_estrutura_turnos(data_inicio, dias)
        df_alertas = self.gerar_volumetria_alertas(data_inicio, dias, estresse)
        
        return {
            'analistas': df_analistas,
            'turnos': df_turnos,
            'alertas': df_alertas
        }

# --- Bloco de Execução Exclusiva (Testes de Validação) ---
if __name__ == "__main__":
    gerador = GeradorInstanciasNOC(seed=2026)
    
    # 1. Simulação do Cenário de Controle (Operação Estável)
    cenario_normal = gerador.gerar_instancia_completa(data_inicio="2026-07-01", dias=7, qtd_analistas=10, estresse=False)
    print("--- CENÁRIO NORMAL ---")
    print(f"Total de Analistas Cadastrados: {len(cenario_normal['analistas'])}")
    print(f"Volume Total de Alertas Gerados: {len(cenario_normal['alertas'])}")
    
    # 2. Simulação do Cenário de Estresse (Sobrecarga de Infraestrutura)
    cenario_crise = gerador.gerar_instancia_completa(data_inicio="2026-07-01", dias=7, qtd_analistas=10, estresse=True)
    print("\n--- CENÁRIO DE ESTRESSE ---")
    print(f"Volume Total de Alertas Gerados na Crise: {len(cenario_crise['alertas'])}")
    
    # Exibição de amostra dos dados estruturados para conferência
    print("\nExemplo da Estrutura de Alertas para o Motor Algorítmico:")
    print(cenario_crise['alertas'].head())
