import os

#limpar terminal sem me atrapalhar:
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
try:
    print('\n   Olá! Seja muito bem-vindo/a a tabuada do Henderson!')

    print('\n1 - Iniciar')
    print('2 - Sair\n')

    escolha = int(input('Digite a sua escolha:  '))

    if escolha == 1:
        numero = int(input('Número para iniciar a operação: '))

        for i in range(0,11):
            print('\nO resultado de', numero, 'X', i, '=', i * numero)

        print('\n\nPrograma finalizado com sucesso!')
        print('\nAté mais!')
        input('\nTecle ENTER para limpar terminal')

        limpar()
    elif escolha == 2:
        limpar()
        print('Até mais!')
    else:
        limpar()
        print('Escolha um número entra 1 e 2!')
except ValueError:
    limpar()
    print('Opção invalida!')