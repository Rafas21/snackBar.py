from treatment import validating_menu

menu = {}

def store_item(qtd):
        for _ in range(qtd):
            typer = input('Tipo: ')
            name = input('Nome: ')
            price = round(float(input('Preco: ')), 1)

            validating_menu(menu, typer, name, price)

def change_item():
    ...