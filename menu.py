from treatment import clear

# Lista do projeto
menu = {
    # "hamburguer": {"Nome": "X-Tudo", "Preco": 20.000},
    # "suco": {"Nome": "Suco de Laranja", "Preco": 7.500}
}

# Verificação de itens
def display_menu():
    clear()
    if not menu:
        input('Nenhum item cadastrado no menu. \nPressione ENTER para retornar...')
        return

    print(f'{'Tipo':<20}{'Nome':<25}{'Preco':>10}{'Qtd':>10}')
    print('-' * 67)

    for tipo, itens in menu.items():
         for item in itens:
            nome = item['nome']
            preco = item['preco']
            quantidade = item['quantidade']
            print(f'{tipo:<20}{nome:<23}R$ {preco:>10.2f}{quantidade:>8}')    
    input('Pressione ENTER para retornar...')
    
def order ():
    ...