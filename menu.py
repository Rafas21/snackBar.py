from treatment import clear

menu = {
    # "hamburguer": {"Nome": "X-Tudo", "Preco": 20.000},
    # "suco": {"Nome": "Suco de Laranja", "Preco": 7.500}
}

def display_menu():
    clear()
    if not menu:
        print('Nenhum item cadastrado no menu. \n')
        return

    print(f'{'Tipo':<20}{'Nome':<25}{'Preco':>10}{'Qtd':>10}')
    print('-' * 55)

    for tipo, itens in menu.items():
         for item in itens:
            nome = item['nome']
            preco = item['preco']
            quantidade = item['quantidade']
            print(f'{tipo:<15}{nome:<20}R$ {preco:>7.2f}{quantidade:>10}')
    print()
