#Bibliotecas ulttilizadas:
from colorama import Fore, Back,  Style
import random
from random import shuffle
while True:
    Style.RESET_ALL
    print(f"{Style.BRIGHT}{Fore.RED}██ {Style.BRIGHT}{Fore.WHITE}██ {Style.BRIGHT}{Fore.BLUE}██\n{Style.BRIGHT}{Fore.RED}██ {Style.BRIGHT}{Fore.WHITE}██ {Style.BRIGHT}{Fore.BLUE}██")
    print(' ')
    print(f'{Style.BRIGHT}{Fore.MAGENTA}PIBIC JR')
    print(f' {Style.BRIGHT}{Fore.CYAN}READER-BRAIDS {Style.RESET_ALL}[1] \n {Style.BRIGHT}{Fore.GREEN}GENERATOR-EQ {Style.RESET_ALL} [2] \n {Style.BRIGHT}{Fore.WHITE}CREDITOS {Style.RESET_ALL}     [3]')
    programa = int(input(f'{Style.BRIGHT}{Fore.CYAN}DIGITE O NUMERO DO PROGRAMA: '))
    Style.RESET_ALL
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if programa == 1:
        print(f'{Fore.CYAN}READER-BRAIDS v1.8')
        print(' ')
        print(f"{Style.BRIGHT}{Fore.RED}██ {Style.BRIGHT}{Fore.WHITE}██ {Style.BRIGHT}{Fore.BLUE}██\n{Style.BRIGHT}{Fore.RED}██ {Style.BRIGHT}{Fore.WHITE}██ {Style.BRIGHT}{Fore.BLUE}██")
        print(' ')
        print(f'{Style.BRIGHT}{Fore.MAGENTA}PIBIC JR')
        print()

        cordas = int(input(f'\n{Style.BRIGHT}{Style.DIM}{Fore.BLUE}QUAL A Qº DE CORDAS? {Style.BRIGHT}{Fore.WHITE} '))  # Indica a quantidade de cordas
        print()
        if cordas == 1:
            print(f'{Style.BRIGHT}{Fore.RED}ERRO')
            continue
        c = 0  # Contador de tranças positivas
        e = 0  # Contador de tranças negativas
        f = 0  # Contador de tranças triviais
        movimentos = []
        # Solicitando o sinal do sigma de cada corda
        while True:
            corda = int(input(f'{Style.BRIGHT}{Fore.CYAN}QUAL O Nº DA CORDA?{Style.BRIGHT}{Fore.WHITE} '))
            if corda == cordas:
                print(f'{Style.BRIGHT}{Fore.RED}ERRO')
                continue
            if corda >= cordas:
                print(f'{Style.BRIGHT}{Fore.RED}ERRO')
                continue
            if corda <= 0:
                print(f'{Style.BRIGHT}{Fore.RED}ERRO')
                continue
            sigma= int(input(f'{Style.BRIGHT}{Fore.GREEN} QUAL O SIGMA DA {Style.BRIGHT}{Fore.WHITE}{corda}? '))
            if sigma == 1:
                Style.RESET_ALL
                movimentos.append(f'A {corda} PASSOU PELA FRENTE DA {corda+1}')
            elif sigma == -1:
                movimentos.append(f'A {corda} PASSOU POR TRÁS DA {corda+1}')
            elif sigma == 0:
                break
        print(f'{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{movimentos}')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if programa == 2:
        #DeBug nas cores e estilos do console:
        Style.RESET_ALL
        #Creditos:
        print(f'{Style.BRIGHT}{Fore.GREEN}GENERATOR-EQ v2.3')
        Style.RESET_ALL
        print(f"{Style.BRIGHT}{Fore.RED}██ {Style.BRIGHT}{Fore.WHITE}██ {Style.BRIGHT}{Fore.BLUE}██\n{Style.BRIGHT}{Fore.RED}██ {Style.BRIGHT}{Fore.WHITE}██ {Style.BRIGHT}{Fore.BLUE}██")
        print(' ')
        print(f'{Style.BRIGHT}{Fore.MAGENTA}PIBIC JR')
        #Variaveis principais:
        cordas = int(input(f'\n{Style.BRIGHT}{Style.DIM}{Fore.BLUE}DIGITE A Qº DE CORDAS: '))
        nomeTO = []
        equivalente = []
        probabilidade = 1
        n = cordas
        r=1
        c=1
        qsigma = 0
        #identificador de corda e sigma:
        Style.RESET_ALL
        while True:
            print(' ')
            i = int(input(f'{Style.BRIGHT}{Fore.CYAN}DIGITE O Nº DA CORDA: '))
            if i == n:
                break
            if i == 0:
                print(f'{Style.BRIGHT}{Fore.RED}ERRO')
                continue
            Style.RESET_ALL

            sigma = int(input(f'{Style.BRIGHT}{Fore.GREEN}DIGITE O SIGMA DA CORDA{Style.BRIGHT}{Fore.WHITE} {i}: '))
            if sigma == 0:
                Style.RESET_ALL
                print(f'{Style.BRIGHT}{Fore.RED}ERRO')
                continue
            elif sigma != 1 and sigma != -1:
                print('erro')
                continue
            else:
                #Armazenador de dados:
                Style.RESET_ALL
                nomeTO.append(f'a{i}^{sigma}')
                equivalente.append(f'a{i}^{-1*sigma}')
                qsigma += 1
        #DeBug de novo(?):
        Style.RESET_ALL
        while c <= qsigma:
            r *= c
            c += 1
        for j in range(1,r):
            random.shuffle(equivalente)
            print(f'{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}EQUIVALENTES {Style.RESET_ALL}{j}{Fore.GREEN}:  {Style.BRIGHT}{Fore.YELLOW}{equivalente}')
            probabilidade += 1
        print(f'{Style.BRIGHT}{Fore.BLUE}TRANÇA ORIGINAL: {Style.RESET_ALL}{Style.BRIGHT}{nomeTO}')
        print(f'{Style.BRIGHT}{Fore.CYAN}EQUIVALENTES GERADAS: {Style.RESET_ALL}{Style.BRIGHT}{probabilidade}')
        Style.RESET_ALL
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if programa == 3:
        print(f'{Style.BRIGHT}{Fore.BLUE}DEV: @evandro.linss \n    evandrojardiel@gmail.com')
        print(f'{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}PIBIC JR: pibicjr.msg@gmail.com')
        continue