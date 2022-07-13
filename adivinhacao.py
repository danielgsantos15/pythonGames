import jogos
import random


def jogar():
    print('***************************')
    print('****Jogo de advinhaçaõ!****')
    print('***************************')

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print('Escolha o nível de dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        str_chute = input('Digite um número: ')
        print('Você digitou', str_chute)
        chute = int(str_chute)

        if chute < 1 or chute > 100:
            print('Digite um número de 1 até 100')
            continue

        acertou = chute == numero_secreto
        chute_alto = chute > numero_secreto
        chute_baixo = chute < numero_secreto

        if acertou:
            print('Você acertou! fez {} pontos!'.format(pontos))
            break
        else:
            if chute_alto:
                print('Chutou alto!')
                if rodada == total_de_tentativas:
                    print('O número secreto era {}, você fez {} pontos!'.format(numero_secreto, pontos))
            elif chute_baixo:
                print('Chutou baixo!')
                if rodada == total_de_tentativas:
                    print('O número secreto era {}, você fez {} pontos!'.format(numero_secreto, pontos))
            pontos = pontos - abs(chute - numero_secreto)

    print('Fim do jogo!')

    print('Jogar novamente?')
    novo_jogo = int(input('(1) SIM (2) NÃO: '))

    if novo_jogo == 1:
        jogar()
    else:
        jogos.escolher()
        print('Obrigado por jogar!')


if __name__ == '__main__':
    jogar()
