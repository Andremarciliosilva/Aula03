### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

import csv
dict: list = []

with open('dados.csv', 'r' ) as csvdados:
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
