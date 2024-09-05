print('Insira as quatro notas bimestrais para calcular a média: ')
#Entrada de dados
primeira_nota = float(input('Insira a primeira nota: '))
segunda_nota = float(input('Insira a segunda nota: '))
terceira_nota = float(input('Insira a terceira nota: '))
quarta_nota = float(input('Insira a quarta nota: '))
#Calculo da média
media_nota = primeira_nota + segunda_nota + terceira_nota + quarta_nota / 4 
#Impressão do resultado
print(f'A média foi: {media_nota}')