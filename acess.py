from menu import store_item
from order import display_menu

def adm_acess():
    while True:
        print('Funções')
        print()

        choose = input('O que deseja fazer ?')

        match choose:
            case '1':
                try:
                    qtd = int(input('Quantos itens deseja cadastrar? '))
                    store_item(qtd)
                except ValueError:
                    print('Digite um número válido.')

            case '2':
                return display_menu()
                

            case '0':
                print('Saindo do menu administrador...')
                break

            case _:
                return 'Escolha inexistente'

def client_acess():
    ...
