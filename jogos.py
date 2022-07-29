import adivinhacao
import forca
import jogo_da_velha


def escolher():
    print('***************************')
    print('*****Escolha um jogo!******')
    print('***************************')

    print('(1) Forca (2) Adivinhação (3) Jodo da Velha')
    jogo = int(input('O que você quer jogar?'))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()

    elif jogo == 2:
        print('Jogando Adivinhação')
        adivinhacao.jogar()
    
    elif jogo == 3:
        print('Jogando Jogo da Velha')
        jogo_da_velha.jogar()


if __name__ == '__main__':
    escolher()
