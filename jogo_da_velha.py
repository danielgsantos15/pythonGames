moves = 0
# game_table = ['1', '2', 'X', 'O', 'X', 'X', 'X', 'O', 'X']
game_table = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
players = []


def controla_rodadas():
    for value in game_table:
        if value == 'X' or value == 'O':
            value = True
            print(value)
        else:
            value = False
    return


controla_rodadas()


def apresenta_jogo():
    print('*****************************')
    print('********JOGO DA VELHA********')
    print('*****************************')


apresenta_jogo()


def recebe_jogadores():
    players.append(input('Nome do jogador 1: '))
    players.append(input('Nome do jogador 2: '))
    return players


recebe_jogadores()


def mostra_tabuleiro():
    print('  {}  |  {}  |  {}  '.format(game_table[0], game_table[1], game_table[2]))
    print('-----|-----|-----')
    print('  {}  |  {}  |  {}  '.format(game_table[3], game_table[4], game_table[5]))
    print('-----|-----|-----')
    print('  {}  |  {}  |  {}  '.format(game_table[6], game_table[7], game_table[8]))


def recebe_jogadas():
    if moves % 2 == 0:
        print('Vez de {} (X)'.format(players[0]))
        table_position = int(input('Escolha uma posição: '))
        if table_position <= 0 or table_position > 9:
            print('')
            print('*****Insira um número de 1 a 9 *****')
        else:
            position = table_position - 1
            if game_table[position] == 'X' or game_table[position] == 'O':
                print('')
                print('*****Lugar Ocupado*****')
            else:
                game_table.pop(position)
                game_table.insert(position, 'X')
    else:
        print('Vez de {} (O)'.format(players[1]))
        table_position = int(input('Escolha uma posição: '))
        if table_position <= 0 or table_position > 9:
            print('')
            print('*****Insira um número de 1 a 9 *****')
        else:
            position = table_position - 1
            if game_table[position] == 'X' or game_table[position] == 'O':
                print('')
                print('*****Lugar Ocupado*****')
            else:
                game_table.pop(position)
                game_table.insert(position, 'O')


def mostra_ganhador(player):
    mostra_tabuleiro()
    print('******{} venceu!******'.format(player))


while moves < 9:
    mostra_tabuleiro()
    recebe_jogadas()

    if moves == 8:
        mostra_tabuleiro()
        print('****Deu velha****')
        break

    moves += 1

    if game_table[0] == 'X' and game_table[1] == 'X' and game_table[2] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[3] == 'X' and game_table[4] == 'X' and game_table[5] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[6] == 'X' and game_table[7] == 'X' and game_table[8] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[0] == 'X' and game_table[3] == 'X' and game_table[6] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[1] == 'X' and game_table[4] == 'X' and game_table[7] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[2] == 'X' and game_table[5] == 'X' and game_table[8] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[0] == 'X' and game_table[4] == 'X' and game_table[8] == 'X':
        mostra_ganhador(players[0])
        break
    if game_table[2] == 'X' and game_table[4] == 'X' and game_table[6] == 'X':
        mostra_ganhador(players[0])
        break

    if game_table[0] == 'O' and game_table[1] == 'O' and game_table[2] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[3] == 'O' and game_table[4] == 'O' and game_table[5] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[6] == 'O' and game_table[7] == 'O' and game_table[8] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[0] == 'O' and game_table[3] == 'O' and game_table[6] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[1] == 'O' and game_table[4] == 'O' and game_table[7] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[2] == 'O' and game_table[5] == 'O' and game_table[8] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[0] == 'O' and game_table[4] == 'O' and game_table[8] == 'O':
        mostra_ganhador(players[1])
        break
    if game_table[2] == 'O' and game_table[4] == 'O' and game_table[6] == 'O':
        mostra_ganhador(players[1])
        break
