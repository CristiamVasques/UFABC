from datetime import date

# Data de nascimento
ano_nasc = int(input("Em que ano você nasceu? "))
mes_nasc = int(input("Qual o mês do seu aniversário (somente números)? "))
dia_nasc = int(input("Qual o dia dos seu aniversário? "))

data_nasc = date(ano_nasc, mes_nasc, dia_nasc)

# Data de hoje
hoje = date.today()

# Calcula a idade
idade = hoje.year - data_nasc.year

# Ajusta se ainda não fez aniversário neste ano
if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
    idade -= 1

# Descobre o dia da semana
# %A retorna o nome completo do dia (segunda-feira, terça-feira, etc.)
dia_semana_ingles = data_nasc.strftime("%A")

# Dicionário para traduzir para português
dias_semana_pt = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

# Tradução
dia_semana_pt = dias_semana_pt[dia_semana_ingles]

print(f"Idade: {idade} anos")
print(f"Dia da semana no nascimento: {dia_semana_pt}")
