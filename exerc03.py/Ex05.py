import re
from datetime import datetime

# Função para calcular o valor da gorjeta
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula a gorjeta com base no valor da conta e na porcentagem informada.
    """
    return valor_conta * (porcentagem_gorjeta / 100)

# Função para verificar se uma palavra ou frase é um palíndromo
def eh_palindromo(texto: str) -> str:
    """
    Verifica se o texto é um palíndromo, ignorando espaços e pontuações.
    """
    # Remove tudo que não for letra ou número e converte para minúsculo
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    # Compara o texto com ele mesmo invertido
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Função para calcular idade aproximada em dias
def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade aproximada em dias com base no ano de nascimento.
    (Não considera anos bissextos)
    """
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

# Menu principal do programa
def menu():
    while True:
        print("\n=== Menu de Funções ===")
        print("1. Calcular gorjeta")
        print("2. Verificar se é palíndromo")
        print("3. Calcular idade em dias")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Digite o valor da conta (R$): "))
                porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))
                gorjeta = calcular_gorjeta(valor, porcentagem)
                print(f"Gorjeta: R${gorjeta:.2f}")
            except ValueError:
                print("Entrada inválida. Use números válidos.")

        elif opcao == "2":
            texto = input("Digite a palavra ou frase: ")
            resultado = eh_palindromo(texto)
            print(f"É palíndromo? {resultado}")

        elif opcao == "3":
            try:
                ano = int(input("Digite o ano de nascimento: "))
                dias = calcular_idade_em_dias(ano)
                print(f"Idade aproximada em dias: {dias}")
            except ValueError:
                print("Ano inválido. Digite um número inteiro.")

        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu ao executar o script
if __name__ == "__main__":
    menu()