from menu import display_menu, menu, order
from treatment import clear, store_item

# Funções do administrador
def adm_acess():
    while True:
        choose = input('Funções \n\n1 - Cadastrar produto \n2 - Verificar estoque \n3 - Voltar ao menu \n\nO que deseja fazer ? ')
        if choose == '1':
            try:
                clear()
                qtd = int(input('Quantos itens deseja cadastrar? '))
                store_item(qtd, menu)

            except ValueError:
                clear()
                print('Digite um número válido.')
                continue

        elif choose == '2':
            display_menu()

        elif choose == '3':
            clear()
            print('Indo para o menu...')
            break

        else:
            clear()
            return 'Escolha inexistente'

# Funções do cliente
def client_acess():
    while True:
        choose = input('O que deseja fazer ?\n\n1 - Olhar o menu\n2 - Fazer pedido')
        if choose == '1':
            display_menu()

        elif choose == '2':
            order()
        else:
           clear()
            return 'Escolha inexistente' 