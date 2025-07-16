from menu import store_item

def adm_acess():
    while True:
        print('Funções')
        print()
        choose = input('O que deseja fazer ?')

        if choose == '1':
                try:
                    qtd = int(input('Quantos itens deseja cadastrar? '))
                    return store_item(qtd)
                except ValueError:
                    print('Digite um número válido.')

        if choose == '2':
            return

        if choose == '0':
            print('Saindo do menu administrador...')
            break

        else:
            print('Escolha inexistente')

def client_acess():
    ...
