def estoqueExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True

def criarEstoque(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()

    except:
        print("Houve um erro durante a criação do arquivo.")

    else:
        print(f'Arquivo {arquivo} criado com sucesso.')

def listarBebidasEstoque(arquivo):
    try:
        a = open(arquivo, 'rt')

    except:
        print('Erro ao ler o arquivo')

    else:
        print("\033[1;97m QTD. NOME                           PREÇO\033[m")
        for linha in reversed(list(open("Estoque.txt"))):
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:>4}x {dado[1]:<30} R${dado[2]:>3}')

    finally:
        a.close()

def cadastrarBebidasEstoque(arquivo, nome, preco, quantidade):
    try:
        a = open(arquivo, 'at')

    except:
        print('Houve um erro na abertura do arquivo!')

    else:
        try:
                a.write(f'{quantidade};{nome};{preco}\n')
        except:
            pass

        else:
            print(f'Novo registro de {nome} adicionado.\n')
            a.close()
