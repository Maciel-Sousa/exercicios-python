def classificador_idade():
    idade = int(input("Digite sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Você é uma Criança.")
    elif idade <= 17:
        print("Você é um Adolescente.")
    elif idade <= 59:
        print("Você é um Adulto.")
    elif idade >= 60:
        print("Você é um Idoso.")
    else:
        print("Idade inválida.")


def calculadora_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura * altura)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obeso")


def conversor_temperatura():
    temperatura = float(input("Digite a temperatura: "))
    origem = input("De qual unidade? (C/F/K): ").upper()
    destino = input("Para qual unidade? (C/F/K): ").upper()

    resultado = None

    if origem == "C":
        if destino == "F":
            resultado = (temperatura * 9/5) + 32
        elif destino == "K":
            resultado = temperatura + 273.15
        else:
            resultado = temperatura
    elif origem == "F":
        if destino == "C":
            resultado = (temperatura - 32) * 5/9
        elif destino == "K":
            resultado = (temperatura - 32) * 5/9 + 273.15
        else:
            resultado = temperatura
    elif origem == "K":
        if destino == "C":
            resultado = temperatura - 273.15
        elif destino == "F":
            resultado = (temperatura - 273.15) * 9/5 + 32
        else:
            resultado = temperatura

    if resultado is not None:
        print(f"Temperatura convertida: {resultado:.2f}°{destino}")
    else:
        print("Unidade inválida.")


def verificador_bissexto():
    ano = int(input("Digite um ano: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")


# MENU PRINCIPAL
while True:
    print("\n=== MENU DE OPÇÕES ===")
    print("1 - Classificador de Idade")
    print("2 - Calculadora de IMC")
    print("3 - Conversor de Temperatura")
    print("4 - Verificador de Ano Bissexto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        classificador_idade()
    elif opcao == "2":
        calculadora_imc()
    elif opcao == "3":
        conversor_temperatura()
    elif opcao == "4":
        verificador_bissexto()
    elif opcao == "0":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
