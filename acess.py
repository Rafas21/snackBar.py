from menu import display_menu, menu
from treatment import clear, store_item

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

        if choose == '2':
            display_menu()

        if choose == '3':
            clear()
            print('Indo para o menu...')
            break

        else:
            clear()
            return 'Escolha inexistente'

def client_acess():
    ...
