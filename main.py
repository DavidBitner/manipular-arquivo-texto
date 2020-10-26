def separador():
    print('*' * 50)


def print_centralizado(txt):
    print(f'{txt}'.center(50))


def print_personalizado(txt):
    print('*' * 50)
    print_centralizado(txt)
    print('*' * 50)


def gerar_numero(txt='lul'):
    entrada = int(input(txt))
    return entrada


def adicionar_texto():
    separador()
    append = str(input('Escreva o que deseja adicionar ao arquivo:\n'))
    with open('main.txt', 'a') as arquivo:
        arquivo.write(f'{append}\n')
    print('Texto adicionado com sucesso')


def ver_conteudo():
    separador()
    with open('main.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    input('Pressione enter para continuar...')


def ver_conteudo_linha():
    pass


def procurar():
    pass


def deletar():
    pass


# Main
opcoes = ['1 - Adicionar texto', '2 - Ver conteudo do arquivo', '3 - Ver conteudo de uma linha especifica',
          '4 - Procurar por sentenças', '5 - Deletar texto', '69 - Sair']
separador()
print_centralizado('BEM VINDO')
while True:
    separador()
    print('Selecione uma das opções')
    for o in opcoes:
        print(o)
    separador()
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
        print_personalizado('Até logo')
        break
