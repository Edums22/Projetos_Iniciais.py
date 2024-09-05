def romano_para_inteiro(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in romano[::-1]:
        valor = valores[char]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor
    return total

numero_romano = input("Digite um número romano: ")
print(f"O número {numero_romano} em inteiro é {romano_para_inteiro(numero_romano)}")
