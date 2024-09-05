#Entrada de dados
print("-=-" * 20)
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("-=-" * 20)
#Resultados nome
print(f"\nSeu nome é {nome}.")
print("-" * 30)
print("Seu nome invertido é:",nome[::-1])
print("-" * 30)
if " " in nome:
    print("Seu nome contém espaços.")
    print("-" * 30)
else:
    print("Seu nome não contém espaços.")
    print("-" * 30)
    print(len(nome),("é o número de letras do seu nome"))
    print("-" * 30)
    print("A primeira letra do seu nome é:", nome[0])
    print("-" * 30)
    print("A última letra do seu nome é:", nome[-1])
    print("-" * 30)
#Resultados idade
print(f"Sua idade é {idade}")
print("-" * 30)
print("Sua idade invertida é ", idade[::-1])
print("-" * 30)
print("O primeiro digito da sua idade é:",idade [0])
print("-" * 30)
print("O último dígito da sua idade é:", idade[-1])
print("-=-" * 20)

