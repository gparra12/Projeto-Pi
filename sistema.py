from lib.arquivo import *
from time import sleep
from lib.interface import *

arquivo = 'Estoque.txt'

if not estoqueExiste(arquivo):
    criarEstoque(arquivo)

while True:
    cabecalho('\033[1;97mDELIVERY\033[m')

    resposta = menu(['Cadastrar', 'Listar', 'Sair do Sistema'])
    if resposta == 1:
        numeroCadastros = int(input(("Quantas bebidas deseja cadastrar? ")))

        while numeroCadastros != 0:
            nome = input("Informe o nome da bebida: ").capitalize()
            preco = float(input("Informe o preço da bebida: "))
            quantidade = leitorDeInt("Agora, a quantidade: ")
            numeroCadastros -= 1
            cadastrarBebidasEstoque(arquivo, nome, preco, quantidade)

    elif resposta == 2:
        print("Listando", end='')
        etc = '.....'
        for i in range(5):
            print(etc[i], sep='', end='', flush=True)
            sleep(0.5)
        sleep(0.5)
        print('\n')
        listarBebidasEstoque(arquivo)

    elif resposta == 0:
        print("\n")
        cabecalho("\033[1;97mSaindo do sistema... Até logo!\033[m")
        break

    else:
        print("\033[31mERRO! Opção inválida! Por favor digite novamente: \033[m")

    sleep(0.5)