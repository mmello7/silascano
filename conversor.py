def dolar_real():
    try:
        dolar = float(input("Digite o valor em dólar: "))
        real = dolar * 5.25  # Valor de conversão atualizado
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def euro_real():
    try:
        euro = float(input("Digite o valor em euro: "))
        real = euro * 6.22
        print(f"O valor em reais é R${real:.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")

def libra_real():
    try:
        libra = float(input("Digite o valor em libra: "))
        real = libra * 7.42
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

def real_yuan():
    try:
        real = float(input("Digite o valor em reais: "))
        yuan = real / 0.82
        print(f"O valor em yuan é ¥{yuan:.2f}")
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