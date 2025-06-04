#Crie um script em Python que escreva dados em um arquivo CSV. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​

import csv

def escrever_csv(nome_arquivo, dados):

    colunas = ["Nome", "Idade", "Cidade"]

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")


dados_pessoas = [
    {"Nome": "Luciana", "Idade": 30, "Cidade": "São Bernardo do Campo"},
    {"Nome": "Cristiana", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Ana Paula Monteiro", "Idade": 22, "Cidade": "São Paulo"}
]
    
escrever_csv("dados_pessoas.csv", dados_pessoas)
# O código acima cria um arquivo CSV chamado "dados_pessoas.csv" com as informações de pessoas.

