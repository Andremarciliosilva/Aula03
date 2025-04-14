

print('''Exercício 1: Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir 
que todos os registros tenham valores positivos para `quantidade` e `preço`. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
forem positivos ou "Dados inválidos" caso contrário.''')
print ('\n')

print('Lendo arquivo csv')
print('Resultado:')

import csv
dict: list = []

print('Primeira resolução')
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

print('Segunda resolução')
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

print ('\n')
print('''Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'
Temperatura inserida para teste: 17°C
''')
print ('\n')

temp_baixa = 18
temp_normal = range(18,26)
temp_alta = 30

temp_atual = 17

if temp_atual < 18:
    print('A temperatura está baixa')

elif temp_atual in temp_normal:
    print('A temperatura está normal')

else:
    print('A temperatura está alta')

print ('\n')
print('''Exercício 3: Filtragem de Logs por Severidade
Você está analisando logs de uma aplicação e precisa filtrar mensagens 
com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
''')
print ('\n')

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

for i in log.values():
    if i == 'ERROR':
        print(i)

print ('\n')
print ('''Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
fornecido um email válido. Escreva um programa que valide essas condições 
e imprima "Dados de usuário válidos" ou o erro específico encontrado.
Dados inserivos para teste:
idade = 30
email = 'andresilva@gmail.com'
''')
print ('\n')
idade = 30
email = 'andresilva@gmail.com'

if idade in range(18,65) and '@' in email:
    print('Dados de usuário válidos')
else:
    print('Dados de usuário inválidos')

print ('\n')
print(''' Exercício 5: Detecção de Anomalias em Dados de Transações
Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
''')
print ('\n')

transacao = {'valor': 10000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] not in range(9,19):
    print('Nao ok')
else:
    print('OK')

print ('\n')
print('''Exercício 6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
Texto inserido para teste: "a a a a a raposa marrom salta sobre o o o o cachorro preguiçoso"
''')
print ('\n')

texto = "a a a a a raposa marrom salta sobre o o o o cachorro preguiçoso"
lista: list = texto.split()
contagem_palavras = {}

print(lista)

for i in lista:
    if i in contagem_palavras:
        contagem_palavras[i] += 1
    else:
        contagem_palavras[i] = 1
    
print(contagem_palavras)

print ('\n')
print ('''Exercício 7. Normalização de Dados
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
Lista de números inseridas para teste: numeros = [10, 20, 30, 40, 50]
''')
print ('\n')

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

print ('\n')
print('''Exercício 8. Filtragem de Dados Faltantes
Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
Dicionários inseridos para teste: 
      usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]
''')
print ('\n')

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

for d in usuarios:
    for k, v in d.items():
        if v == '':
            print(f'O usuário {d['nome']} tem campo faltando')

print ('\n')
print('''Exercício 9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
Dados inseridos para teste: lista: list = range(1,30)
''')
print ('\n')

lista: list = range(1,30)

for n in lista:
    if n % 2 == 0:
        print(n)

print ('\n')
print('''Exercício 10. Agregação de Dados por Categoria.
Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
Dados inseridos para teste:
      vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
''')
print ('\n')

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

vendas_categoria = {}

for v in vendas:
    categoria = v['categoria']
    valor = v['valor']

    if categoria in vendas_categoria:
     vendas_categoria[categoria] += valor

    else:
      vendas_categoria[categoria] = valor

print(vendas_categoria)

print ('\n')
print('''Exercício 11. Leitura de Dados até Flag
Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
''')
print ('\n')

while True:
    flag = input('Digite alguma coisa pra continuar ou sair pra sair do programa:')
    if flag == 'sair':
        break

print ('\n')
print('''Exercício 12. Validação de Entrada.
Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
''')
print ('\n')

while True:

    entrada = int(input('Digite um número entre 0 e 10:'))
    if entrada in range(0,11):
        break
    else:
        continue

print ('\n')
print('''Exercício 13. Consumo de API Simulado.
Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
Dados inseridos para teste:
pagina_atual = 0
paginas_totais = 10
''')
print ('\n')

pagina_atual = 0
paginas_totais = 10

while pagina_atual <= paginas_totais :

    print(f'Consumindo pagina {pagina_atual} de {paginas_totais} paginas totais' )
    pagina_atual += 1

print ('\n')
print('''Exercício 14. Tentativas de Conexão
Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
Dados inseridos para teste:
tentativa = 0
limite_tentativas = 15
''')
print ('\n')

tentativa = 0
limite_tentativas = 15

while tentativa <= limite_tentativas:
    print(f'Tentativa de conexão {tentativa} de {limite_tentativas} tentativas')
    tentativa += 1

print ('\n')
print('''Exercício 15. Processamento de Dados com Condição de Parada
Processar itens de uma lista até encontrar um valor específico que indica a parada.
Dados inseridos para teste:
itens = [1, 2, 3, "parar", 4, 5]
''')
print ('\n')

itens = [1, 2, 3, "parar", 4, 5]

for i in itens:
    if i == 'parar':
        print('Valor encontrado')
        break
    else:
        print(i)
