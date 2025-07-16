from treatment import validating_menu

menu = {
    "hamburguer": {"nome": "X-Tudo", "preco": 20.000},
    "suco": {"nome": "Suco de Laranja", "preco": 7.500}
}

def store_item(qtd):
        for _ in range(qtd):
            typer = input('Tipo: ')
            name = input('Nome: ')
            price = input('Preco: ')
            amount = 0

            validating_menu(menu, typer, name, price, amount)

def order(item):
    if item not in menu:
        print('Item nao existe ou nao foi cadastrado')

def display_menu():
    print(f"{'Tipo':<20}{'Nome':<25}{'Preço':>10}")
    print('-' * 55)

    for tipo, info in menu.items():
        name = info['nome']
        preco = info['preco']
        print(f"{tipo:<20}{name:<25}R$ {preco:>7}")
