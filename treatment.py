import os
from acess import adm_acess

def clear():
    os.system('cls')

def check_password():
    senha_correta = 'adm@21'

    while True:
        senha = input('Digite a senha de administrador: ')
        if senha == senha_correta:
            clear()
            print('Acesso concedido.')
            adm_acess()

        else:
            clear()
            print('Senha incorreta. Tente novamente.')
        continue

