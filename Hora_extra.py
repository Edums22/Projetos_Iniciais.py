#ENTRADA DE DADOS
valor_salario = float(input("Digite o valor do seu salário: ")) 
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados no mês: "))
horas = float(input("Digite as horas trabalhadas por dia: "))
hora_extra = float(input("Digite a quantidade de horas extra por mês: "))

#CALCULOS
valor_dia = valor_salario / dias_trabalhados
valor_hora = valor_dia / horas
valor_extra = hora_extra * valor_hora

#EXIBIÇÃO DO RESULTADO
print(f"\nO valor da sua diária é: R$",valor_dia)
print(f"Seu valor por hora é: R$",valor_hora)
print(f"Suas horas extras totalizam em: R$",valor_extra)
print(f"O valor do seu salário somado a hora extra fica: R$",valor_salario + valor_extra)