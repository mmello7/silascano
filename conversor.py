def dolar_real():
    try:
        dolar = float(input("Digite o valor em dólar: "))
        real = dolar * 5.25  # Valor de conversão atualizado
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_dolar():
    try:
        real = float(input("Digite o valor em reais: "))
        dolar = real / 5.25  # Valor de conversão atualizado
        print(f"O valor em dólar é US${dolar:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def euro_real():
    try:
        euro = float(input("Digite o valor em euro: "))
        real = euro * 6.22
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_euro():
    try:
        real = float(input("Digite o valor em reais: "))
        euro = real / 6.22
        print(f"O valor em euro é €{euro:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def libra_real():
    try:
        libra = float(input("Digite o valor em libra: "))
        real = libra * 7.42
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_libra():
    try:
        real = float(input("Digite o valor em reais: "))
        libra = real / 7.42
        print(f"O valor em libra é £{libra:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def yen_real():
    try:
        yen = float(input("Digite o valor em yen: "))
        real = yen * 0.038
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_yen():
    try:
        real = float(input("Digite o valor em reais: "))
        yen = real / 0.038
        print(f"O valor em yen é ¥{yen:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def yuan_real():
    try:
        yuan = float(input("Digite o valor em yuan: "))
        real = yuan * 0.82
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_yuan():
    try:
        real = float(input("Digite o valor em reais: "))
        yuan = real / 0.82
        print(f"O valor em yuan é ¥{yuan:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def won_real():
    try:
        won = float(input("Digite o valor em won: "))
        real = won * 0.0041
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_won():
    try:
        real = float(input("Digite o valor em reais: "))
        won = real / 0.0041
        print(f"O valor em won é ₩{won:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def real_menu():
    print("1 - Dólar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Yen")
    print("5 - Yuan")
    print("6 - Won")
    print("0 - Voltar ao menu principal")

    opcao_real = int(input("Escolha uma opção: "))
    if opcao_real == 1:
        real_dolar()
    elif opcao_real == 2:
        real_euro()
    elif opcao_real == 3:
        real_libra()
    elif opcao_real == 4:
        real_yen()
    elif opcao_real == 5:
        real_yuan()
    elif opcao_real == 6:
        real_won()
    elif opcao_real == 0:
        pass
    else:
        print("Opção inválida")


def estrangeiro_menu():
    print("1 - Dólar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Yen")
    print("5 - Yuan")
    print("6 - Won")
    print("0 - Voltar ao menu principal")

    opcao_estrangeiro = int(input("Escolha uma opção: "))
    if opcao_estrangeiro == 1:
        dolar_real()
    elif opcao_estrangeiro == 2:
        euro_real()
    elif opcao_estrangeiro == 3:
        libra_real()
    elif opcao_estrangeiro == 4:
        yen_real()
    elif opcao_estrangeiro == 5:
        yuan_real()
    elif opcao_estrangeiro == 6:
        won_real()
    elif opcao_estrangeiro == 0:
        pass
    else:
        print("Opção inválida")

def menu():
    print("1 - Real para moeda estrangeira")
    print("2 - Moeda estrangeira para real")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        real_menu()
    elif opcao == 2:
        estrangeiro_menu()
    elif opcao == 0:
        print("Até mais!")
    else:
        print("Opção inválida")

print(menu())
