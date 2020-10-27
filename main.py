from modules.defs import separador, print_centralizado, gerar_numero, adicionar_texto, ver_conteudo, ver_conteudo_linha
from modules.defs import procurar, deletar, print_personalizado

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
