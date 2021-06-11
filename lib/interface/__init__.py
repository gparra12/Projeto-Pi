def leitorDeInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido. \033[m')
            continue

        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return n

def fazedor_de_linhas(tam=42):
    return '\033[1;33m=\033[m' * tam

def cabecalho(texto):
    if texto == '\033[1;97mDELIVERY\033[m':
        print(fazedor_de_linhas())
        print(texto.center(51))
        print(fazedor_de_linhas())

    elif texto == '\033[1;97mSaindo do sistema... Até logo!\033[m':
        print(fazedor_de_linhas())
        print(texto.center(51))
        print(fazedor_de_linhas())

def menu(lista):
    aux = 1

    for item in lista:
        print(f'\033[1;30m[\033[1;31m{aux}\033[1;30m] \033[1;30m- \033[1;97m{item}\033[m')
        aux += 1
        if aux > 2:
            aux = 0

    print(fazedor_de_linhas())

    opcao = leitorDeInt('\033[1;97mSua opção: \033[m')
    return opcao
