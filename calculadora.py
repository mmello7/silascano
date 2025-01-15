
def soma():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    print(f"O resultado da soma de {x} + {y} é {x + y}")

def subtracao():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    print(f"O resultado da subtração de {x} - {y} é {x - y}")

def multiplicacao():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    print(f"O resultado da multiplicação de {x} X {y} é {x * y}")

def divisao():  
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    print(f"O valor da divisão de {x} por {y} é : {x / y}")

def potencia():
    x = int(input("Digite o valor da base: "))
    y = int(input("Digite o valor do expoente: "))
    print(f"O resultado da exponenciação de {x} por {y} é {x ** y}")

def raiz(): 
    x = int(input("Digite o valor da base: "))
    y = int(input("Digite o valor da raiz: "))
    print(f"O resultado da raiz de {x} por {y} é {x + y}")
    print(f"O valor da raiz de {x} por {y} é {x ** (1/y)}")

def menu():
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz")
    print("7 - Sair")
    return int(input("Digite a opção desejada: "))

while True:
    opcao = menu()
    if opcao == 1:
        print(soma())
    elif opcao == 2:
        print(subtracao())
    elif opcao == 3:
        print(multiplicacao())
    elif opcao == 4:
        print(divisao())
    elif opcao == 5:
        print(potencia())
    elif opcao == 6:
        print(raiz())
    elif opcao == 7:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida")
    

