from menu import store_item
from main import choose

def chooose():
    match choose:
        case 1:
            try:
                number = int(input('Quantos itens deseja cadastrar ? '))
                store_item(number)
            except ValueError:
                return print('Não foi enviado um numero corretamente')
            
        case 2:
            ...