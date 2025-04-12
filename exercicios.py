### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
'''
import csv
dict: list = []

# Primeira resolução
with open('dados.csv', 'r') as csvdados:

    for row in csvdados:
        if row == 'produto,quantidade,preco\n':
            continue
        else:
            lista = row.split(',')
            if int(lista[1]) > 0 and float(lista[2]) > 0:
                print('Dados válidos')
                break
            else:
                print('Dados inválidos')
                break

# Segunda resolução
with open('dados.csv', 'r') as csvdados:
    reader = csv.DictReader(csvdados)

    for row in reader:
        dict.append(row)

for ch in dict:
    ch_int = int(ch['quantidade'])
    ch_qtd = float(ch['preco'])
    if ch_int > 0 and ch_qtd > 0:
        print('Dados válidos')
        break
    else:
        print('Dados inválidos')
        break
'''


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# temp_baixa = 18
# temp_normal = range(18,26)
# temp_alta = 30

# temp_atual = 17

# if temp_atual < 18:
#     print('A temperatura está baixa')

# elif temp_atual in temp_normal:
#     print('A temperatura está normal')

# else:
#     print('A temperatura está alta')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# for i in log.values():
#     if i == 'ERROR':
#         print(i)

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = 30
# email = 'andresilva@gmail.com'

# if idade in range(18,65) and '@' in email:
#     print('Dados de usuário válidos')
# else:
#     print('Dados de usuário inválidos')


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

