# Calculadora de blocos

# Solicitar as dimensões da área
comprimento_area = float(input("Digite o comprimento da área em metros: "))
largura_area = float(input("Digite a largura da área em metros: "))
area_total = float(comprimento_area * largura_area)

# Solicitar as dimensões dos blocos
comprimento_bloco = float(input("Digite o comprimento do bloco em metros: "))
largura_bloco = float(input("Digite a largura do bloco em metros: "))
area_bloco = float(comprimento_bloco * largura_bloco)
num_blocos = float(area_total / area_bloco)
# Exibir o resultado
print(f"Você precisará de aproximadamente {num_blocos:.2f} blocos para cobrir uma área de {area_total:.2f} metros quadrados.")
    


