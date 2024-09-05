#Declaração de Variaveis
nome = input('Digite Seu Nome: ')
altura = float(input('Digite Sua Altura: '))
peso = float(input('Digite Seu Peso: '))
imc = peso / altura ** 2

#Retorno para o usuario
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)