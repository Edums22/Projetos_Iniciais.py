from random import randint
computador = randint(0, 5) #Faz o sorteio entre 0 a 5
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5... Tente adivinhar! ")
print("-=-" * 20)
jogador = int(input("Em que número pensei? ")) #Jogador tenta adivinhar
if jogador == computador:
    print("Parabéns, você conseguiu me vencer!!!")
else:
    print(f"Ganhei! Eu pensei no número {computador} e não no número {jogador}")