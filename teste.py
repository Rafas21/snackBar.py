dados = {}

for _ in range(2):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    # Aqui usamos o nome como chave diretamente
    dados[nome] = {
        'nome': nome,
        'idade': idade
    }

print(dados)