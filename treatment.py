import os

# Adição de intens na lista
def validating_menu(menu, typer, name, price):
    if typer not in menu:
        menu[typer] = []

    for item in menu[typer]:
        if item['nome'].lower() == name.lower():
            item["quantidade"] += 1
            return

    menu[typer].append({
        'nome': name,
        'preco': price,
        'quantidade': 1
    })

# Função clear
def clear():
    os.system('cls')

# Tratamento de senha
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

# Validação da lista
def store_item(qtd, menu):
    for _ in range(qtd):
        clear()
        typer = input('Tipo: ')
        name = input('Nome: ')
        try:
            price = round(float(input("Preço: ")), 2)
        except ValueError:
            print("Preço inválido")
            continue

        validating_menu(menu, typer, name, price)
    clear()