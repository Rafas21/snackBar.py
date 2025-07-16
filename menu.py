from validators import validating_menu

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
