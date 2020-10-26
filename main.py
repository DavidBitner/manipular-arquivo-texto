def linha():
    print('*' * 50)


def gerar_numero(txt='lul'):
    entrada = int(input(txt))
    return entrada


def adicionar_texto():
    pass


def ver_conteudo():
    pass


def ver_conteudo_linha():
    pass


def procurar():
    pass


def deletar():
    pass


# Main
linha()
print('BEM VINDO'.center(50))
while True:
    linha()
    print('Selecione uma das opções')
    print('''1 - Adicionar texto
    2 - Ver conteudo do arquivo
    3 - Ver conteudo de uma linha especifica
    4 - Procurar por sentenças
    5 - Deletar texto''')
    linha()
    opcao = gerar_numero('Entrada: ')
    if opcao == 1:
        adicionar_texto()
    elif opcao == 2:
        ver_conteudo()
    elif opcao == 3:
        ver_conteudo_linha()
    elif opcao == 4:
        procurar()
    elif opcao == 5:
        deletar()
    elif opcao == 69:
        break
linha()
print('Até logo'.center(50))
linha()
