import os
import random

from time import sleep

player = {
    'name': '',

    'x': 0,
    'y': 0,

    'lifes': 10,
    'last_life': 10,

    'points': 0,

    'direction': '',
    'locations': { },
}

game = {
    'running': False,

    'x': 10,
    'y': 5,

    'bombs': { },
    'total': player['lifes'],

    'winner': 10,

    'allowedDirections': {
        'w': True,
        'a': True,
        's': True,
        'd': True,
    },
}

def __init__ ():
    player['name'] = input ('Digite o seu nome: ')

    if (player['name'] != '') and (player['name'] != ' '):
        print (f'Ola { player['name'] } estamos iniciando o jogo, aguarde 3 segundos !')

        __bombs__ ()

        sleep (3.0)
        game['running'] = True
    else:
        print ('Escreva um nome valido.')

    while game['running']:
        __display__ ()

    return True

def __display__ ():
    if (not game['running']):
        return False

    os.system ('cls')

    if (player['lifes'] < 1):
        __show_bombs__ ()

        print ('\n\nVoce perdeu o jogo.')

        sleep (3.5)

        os.system ('cls')
        os._exit (0)
    elif (player['points'] >= game['winner']):
        __show_bombs__ ()

        print ('\n\nVoce venceu o jogo.')

        sleep (3.5)

        os.system ('cls')
        os._exit (0)
    else:
        for y in range (game['y']):
            print ('\n')

            for x in range (game['x']):
                if (player['x'] == x and player['y'] == y):
                    prefix = f'{ player['x'] }@{ player['y'] }'

                    if (prefix in game['bombs']):
                        print ('💣', end = '')
                    else:
                        print ('👻', end = '')
                else:
                    print ('🟩', end = '')

        if (player['last_life'] != player['lifes']):
            print ('\n\nVoce perdeu 1x vida.')
            player['last_life'] = player['lifes']

            sleep (1)

            os.system ('cls')

            del game['bombs'][f'{ player['x'] }@{ player['y'] }']
            __display__ ()
        else:
            player['direction'] = input ('\n\nProxima direcao (w, a, s, d):').lower ()
            __move__ ()
    
    return True

def __move__ ():
    direction = player['direction']

    if (not game['allowedDirections'][direction]):
        return False
    
    if (direction == 'w'):
        player['y'] -= 1
    elif (direction == 'a'):
        player['x'] -= 1
    elif (direction == 's'):
        player['y'] += 1
    elif (direction == 'd'):
        player['x'] += 1

    if (player['x'] < 0):
        player['x'] = (game['x'] - 1)
    elif (player['x'] >= game['x']):
        player['x'] = 0

        if ((player['y'] + 1) >= game['y']):
            player['y'] = 0
        else:
            player['y'] += 1

    if (player['y'] < 0):
        player['y'] = (game['y'] - 1)
    elif (player['y'] >= game['y']):
        player['y'] = 0

    prefix = f'{ player['x'] }@{ player['y'] }'

    if (prefix in game['bombs']):
        player['lifes'] -= 1
    else:
        prefix = f'{ player['x'] }@{ player['y'] }'

        if (prefix in player['locations']):
            return True

        player['points'] += 1
        player['locations'][prefix] = True

    return True

def __bombs__ ():
    column, row = random.randint (0, (game['x'] - 1)), random.randint (0, (game['y'] - 1))
    prefix = f'{ column }@{ row }'

    if (column == 0 and row == 0):
        __bombs__ ()

        return False

    if (prefix in game['bombs'] and len (game['bombs']) < game['total']):
        __bombs__ ()

        return False
    
    game['bombs'][prefix] = True

    if (len (game['bombs']) < game['total']):
        __bombs__ ()

    return True

def __show_bombs__ ():
    for y in range (game['y']):
        print ('\n')

        for x in range (game['x']):
            prefix = f'{ x }@{ y }'

            if (prefix in game['bombs']):
                print ('💣', end = '')
            else:
                print ('🟩', end = '')

__init__ ()