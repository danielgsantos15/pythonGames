import adivinhacao
import forca


def escolher():
    print('***************************')
    print('*****Escolha um jogo!******')
    print('***************************')

    print('(1) Forca (2) Adivinhação')
    jogo = int(input('O que você quer jogar?'))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()

    elif jogo == 2:
        print('Jogando Adivinhação')
        adivinhacao.jogar()


if __name__ == '__main__':
    escolher()
