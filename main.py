from treatment import check_password, clear
from acess import adm_acess, client_acess

print(' -- Bem vindo a Lanchonete PY -- ')
print()

while True:
    print('Você e admnistrador ou cliente ?')
    adm_client = input('Digite [A] para administrador ou [C] para cliente: ').lower()

    if adm_client == 'a':
        clear()
        check_password()
        adm_acess()

    if adm_client == 'c':
        clear()
        continue

    else:
        clear()
        print('Opção digitada não existe, tente novamente!')
        continue