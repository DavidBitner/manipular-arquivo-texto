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
    while True:
        separador()
        posicao_encontrada = []
        entrada = str(input('Insira o que deseja procurar: '))
        with open('main.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        for index, linha in enumerate(linhas):
            if entrada in linha:
                posicao_encontrada.append(index)
        if len(posicao_encontrada) == 0:
            print('Nada encontrado!')
        elif len(posicao_encontrada) == 1:
            print(f'Foi encontrado um resultado na sua busca!')
            print(f'Resultado se encontra na linha {posicao_encontrada[0]}:')
            print(f'{linhas[posicao_encontrada[0]]}')
            continuar()
        elif len(posicao_encontrada) > 1:
            print(f'Foram encontrados {len(posicao_encontrada)} resultados')
            for numero_linha in posicao_encontrada:
                print(f'Linha {numero_linha}:')
                print(f'{linhas[numero_linha]}')
            continuar()
        while True:
            separador()
            voltar = gerar_numero('1 - Realizar mais uma busca\n69 - Voltar\nEntrada: ')
            if voltar == 1 or voltar == 69:
                break
        if voltar == 69:
            break


def deletar():
    while True:
        separador()
        opcoes_del = ['1 - Deletar linha', '2 - Deletar sentença', '3 - Deletar tudo',
                      '69 - Voltar']
        for o_del in opcoes_del:
            print(o_del)
        opcao_del = gerar_numero('Entrada: ')
        if opcao_del == 1:
            separador()
            with open('main.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            for index, linha in enumerate(linhas):
                print(f'{index} - {linha}', end='')
            linha_deletada = gerar_numero('Linha que será apagada: ')
            linhas.pop(linha_deletada)
            with open('main.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha)
            continuar()
        elif opcao_del == 2:
            separador()
            apagar = False
            apagar_quantidade = 0
            with open('main.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            sentenca_deletada = str(input('Digite o que deseja apagar: '))
            for index, linha in enumerate(linhas):
                if sentenca_deletada in linha:
                    nova_linha = linha.replace(f'{sentenca_deletada}', '')
                    linhas[index] = nova_linha
                    apagar = True
                    apagar_quantidade += 1
                    if linhas[index] == '\n':
                        linhas.pop(index)
            if not apagar:
                print('Esta sentença não existe dentro do arquivo de texto!')
            elif apagar:
                with open('main.txt', 'w') as arquivo:
                    for linha in linhas:
                        arquivo.write(linha)
                print(f'Sentença: {sentenca_deletada} apagada com sucesso {apagar_quantidade} ', end='')
                print('vezes') if apagar_quantidade > 1 else print('vez')
            continuar()
        elif opcao_del == 3:
            separador()
            with open('main.txt', 'w') as arquivo:
                arquivo.write('')
            print('Arquivo Limpado com sucesso')
            continuar()
        elif opcao_del == 69:
            break
