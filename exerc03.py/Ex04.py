# 1. Calculadora básica

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            continue

        print("Resultado:", resultado)
        break
    except ValueError:
        print("Erro: entrada não numérica.")


# 2. Registro de notas da turma

notas = []

while True:
    entrada = input("Digite uma nota entre 0 e 10 (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print("Média da turma:", round(media, 2))
else:
    print("Nenhuma nota válida foi inserida.")


# 3. Verificador de senha forte

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte cadastrada.")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e um número.")


# 4. Verificador de par ou ímpar

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: entrada inválida. Digite um número inteiro.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
