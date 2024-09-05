# Calculadora de blocos necessários

def calcular_blocos_necessarios():
    # Solicitar as dimensões da área
    comprimento_area = float(input("Digite o comprimento da área em metros: "))
    largura_area = float(input("Digite a largura da área em metros: "))
    
    # Solicitar as dimensões dos blocos
    comprimento_bloco = float(input("Digite o comprimento do bloco em metros: "))
    largura_bloco = float(input("Digite a largura do bloco em metros: "))
    
    # Calcular a área total a ser coberta
    area_total = comprimento_area * largura_area
    
    # Calcular a área de um bloco
    area_bloco = comprimento_bloco * largura_bloco
    
    # Calcular o número de blocos necessários
    num_blocos = area_total / area_bloco
    
    # Exibir o resultado
    print(f"Você precisará de aproximadamente {num_blocos:.2f} blocos para cobrir uma área de {area_total:.2f} metros quadrados.")
    
# Chamar a função para executar a calculadora
calcular_blocos_necessarios()
