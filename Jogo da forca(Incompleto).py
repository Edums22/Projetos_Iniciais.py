import random

palavras = "Força" "Amizade" "Energia" "Foco " "Perseverança" "Código" "Anime" "Oportunidade"
palavra_secreta = random.choice(palavras)
letras_adivinhadas = []
tentativas = 6
palavara_exibida = ["_" for _ in palavra_secreta] 

while tentativas > 0 and "_" in palavara_exibida:
    print("Palavra: ", " ".join(palavara_exibida))
    print(f"Tentativas restantes: {tentativas}")
    letra = input("Advinhe uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já adivinhou essa letra.")
    elif letra in palavra_secreta:
        print("Correto!")
        letras_adivinhadas.append(letra)
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                palavara_exibida[i] = letra
    else:
        print("Errado!")
        letras_adivinhadas.append(letra)
        tentativas -= 1
        if "_" not in palavara_exibida:
            print("Parabéns, você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)