def validating_menu(menu, typer, name, price, amount):
    if typer and name in menu:
        ...
        
    if not typer and not name in menu:
        return print('Nao foi enviado nenhum item')
                
    if price.isdigit() in menu:
        if not isinstance(price, int):
            return print('Nao foi enviado um valor correto ao produto')

    else:
        menu[typer] = {
        'Nome': name,
        'Preco': price,
        'Quantidade' : amount,
    }