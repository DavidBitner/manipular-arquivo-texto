def separador():
    print('*' * 50)


def print_centralizado(txt):
    print(f'{txt}'.center(50))


def print_personalizado(txt):
    print('*' * 50)
    print_centralizado(txt)
    print('*' * 50)


def continuar():
    input('Pressione enter para continuar...')


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
    continuar()


def ver_conteudo_linha():
    while True:
        separador()
        opcoes_vcl = ['1 - Selecionar linha especifica', '2 - Selecionar um intervalo de linhas', '69 - Voltar']
        for o_vcl in opcoes_vcl:
            print(o_vcl)
        opcao_vcl = gerar_numero('Entrada: ')
        if opcao_vcl == 1:
            separador()
            with open('main.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            print(f'O arquivo possui {len(linhas) + 1} linhas')
            linha_selecionada = gerar_numero('Linha selecionada: ')
            try:
                print(linhas[linha_selecionada - 1])
            except IndexError:
                print_personalizado('Numero acima do limite de linhas do arquivo')
            continuar()
        elif opcao_vcl == 2:
            separador()
            with open('main.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            print(f'O arquivo possui {len(linhas) + 1} linhas')
            primeira_linha = gerar_numero('Primeira linha: ')
            ultima_linha = gerar_numero('Ultima linha: ')
            for i in range(1, len(linhas) + 1):
                if primeira_linha <= i <= ultima_linha:
                    print(f'Linha {i}: {linhas[i - 1]}', end='')
            continuar()
        elif opcao_vcl == 69:
            break


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
