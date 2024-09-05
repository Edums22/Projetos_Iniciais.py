#Declaração de variaveis
tarefas = []

##Menu
def mostrar_menu():
    print("\nMenu Principal")
    print("1. Adicionar tarefa.")
    print("2. Excluir tarefa.")
    print("3. Listar tarefas.")
    print("4. Sair")

def opcao1():
   tarefas = input("Adicione uma tarefa: ")

def opcao2():
    print("Excluir tarefas.")

def opcao3():
    print("Suas tarefas:")

def main():
    while True:
        mostrar_menu()
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            opcao1()
        elif escolha == '2':
            opcao2()
        elif escolha == '3':
            opcao3(list(tarefas))
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
