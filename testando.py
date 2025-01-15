numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

opcao = int(input("Digite um numero de 0 a 20: "))
while opcao < 0 or opcao > 20:
    opcao = int(input("Tente novamente. Digite um número de 0 a 20: "))
print(f"Você digitou o número {numeros[opcao]}")