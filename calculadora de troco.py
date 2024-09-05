preco_unid = float(input("Insira o valor unitário do produto: "))
quant = int(input("Insira a quantidade de produtos "))
valor_pago = float(input("Insira o valor pago "))
#Calculo
custo_total = quant * preco_unid
troco = valor_pago - custo_total
resto = custo_total - valor_pago
#----------------------------------------------------------------------------------------------
if valor_pago >= custo_total:
    print(f"Você comprou {quant} itens, totalizando o valor {custo_total} e seu troco foi {troco}")
else:
    print(f"Falta {resto} para concluir o pagamento")