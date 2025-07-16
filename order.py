from menu import menu

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


display_menu()