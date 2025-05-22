# Conversor de Moeda
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = round(valor_em_reais / taxa_dolar, 2)
valor_em_euro = round(valor_em_reais / taxa_euro, 2)

print("Valor em reais: R$", valor_em_reais)
print("Convertido em dólar: US$", valor_em_dolar)
print("Convertido em euro: €", valor_em_euro)

# Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_do_desconto = round((preco_original * desconto_percentual) / 100, 2)
preco_final = round(preco_original - valor_do_desconto, 2)

print("Produto:", produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", valor_do_desconto)
print("Preço final: R$", preco_final)

# Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = round((nota1 + nota2 + nota3) / 3, 2)

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", media)

# Calculadora de Consumo de Combustível
distancia = 300  # km
combustivel = 25  # litros

consumo_medio = round(distancia / combustivel, 2)

print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio:", consumo_medio, "km/l")

git init
git add Exercicio06.py
git commit -m "Adiciona o exercício 06" 
git remote add origin https://github.com/Maciel-Sousa/exercicios-python.git
git push -u origin main

