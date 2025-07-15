def validating_menu(menu, typer, name, price):
    if name in menu:
        if not typer.isdigit() and not name.isdigit() in menu:
            return print('Item ja adicionado ou não foi enviado nenhum item')
                
    if price in menu:
        if isinstance(price, int):
            return print('Não foi enviado um valor correto ao produto')

    else:
        menu[typer] = {
        'Nome': name,
        'Preco': price,
    }