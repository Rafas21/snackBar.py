from treatment import check_password, clear
from acess import adm_acess, client_acess

# Inicio do projeto
while True:
    adm_client = input(' -- Lanchonete PY --\n\nVocê e admnistrador ou cliente ? \nDigite [A] para administrador ou [C] para cliente: ').strip().lower()
    if adm_client == 'a':
        clear()
        check_password()

        # Repetição de funções do adm
        while True:
            contExit = input('1 - Funções de administrador \n2 - Sair \n\nO que deseja fazer agora ? ')
            clear()

            if contExit == '1':
                adm_acess()

            elif contExit == '2':
                print('Saindo do sistema...')
                break

            else:
                print('Opção não encontrada, tente novamente')
                continue
        break

    # Funções do cliente
    if adm_client == 'c':
        clear()
        client_acess()


        
    # Repetição do inicio
    else:
        clear()
        print('Opção digitada não existe, tente novamente!')
        continue