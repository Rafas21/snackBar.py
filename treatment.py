import os

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

def clear():
    os.system('cls')

def check_password():
    senha_correta = 'adm@21'

    while True:
        senha = input('Digite a senha de administrador: ')
        if senha == senha_correta:
            clear()
            print('Acesso concedido.')
            return
        else:
            clear()
            print('Senha incorreta. Tente novamente.')
        continue