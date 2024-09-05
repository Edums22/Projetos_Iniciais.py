#Menu de operações
print(".1 Adição")
print(".2 Subtração")
print(".3 Multiplicação")
print(".4 Divisão")
print(".5 Sair")

#Seleção de operação
operacao = input("Digite sua escolha (1/2/3/4/5): ")
if operacao == '5':
    print("Saindo...")
    quit()

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacao == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacao == '3':
    print(f"{num1} x {num2} = {num1 * num2}")
elif operacao == '4':
    print(f"{num1} / {num2} = {num1 / num2}")

