itens = []
#Adiciona itens.
def adicionar(item):
    itens.append(item)
    print(f"{item} adicionado a lista.")

#Remove itens.
def remover_item(itemR):
    if itemR in itens:
        itens.remove(itemR)
        print(f"{itemR} removido da lista.")
    else:
        print(f"{itemR} não encontrado na lista.")

#Exibe a lista
def mostrar_lista():
    if itens:
        print("Lista de compras:")
        for i, item in enumerate(itens,start=1):
            print(f"{i}. - {item}")
    else:
        print("Lista de compras vazia.")
#Menu Principal
while True:
    print("\n1. Adicionar item a lista.")
    print("2. Remover item da lista.")
    print("3. Exibir lista de compras")
    print("4. Sair")
    escolha = input("Escolha uma opção (1/2/3/4): ")
    if escolha == '1':
        item = input("Digite um item a ser adicionado: ")
        adicionar(item)
    elif escolha == "2":
        item = input("Digite o item a ser removido: ")
        remover_item(item)
    elif escolha == "3":
        mostrar_lista()
    elif escolha == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção Inválida! Tente novamente.")
        break