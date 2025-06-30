import random

def display_board(l):
    print(f' {l[0]} | {l[1]} | {l[2]} \n'
         '--- --- ---\n'
         f' {l[3]} | {l[4]} | {l[5]} \n'
         '--- --- ---\n'
         f' {l[6]} | {l[7]} | {l[8]} \n')

def has_won(p):
    global game_over
    for win_pos in wins:
        count = 0
        for _pos in win_pos:
            if pos[_pos] == p:
                count += 1
        if count == 3:
            print(f'Player {p} has won with three in a row!')
            game_over = True
            break
        else:
            game_over = False

def play_turn(p):
    check_draw()
    if not game_over:
        num = input(f'Player {p}, where would you like to play? ').strip()
        while num not in pos or num == '':
            num = input('Please enter a valid position to play: ')
        pos[int(num) - 1] = p
        display_board(pos)
        has_won(p)

def bot_play():
    check_draw()
    if not game_over:
        n = random.randint(1, 9)
        while str(n) not in pos:
            n = random.randint(1, 9)
        pos[n - 1] = 'O'
        print(f'The bot has selected position {n}.')
        display_board(pos)
        has_won('O')

def play_again():
    global stop_all
    if game_over:
        if input('Would you like to play again? (y/n): ') == 'n':
            stop_all = True

def check_draw():
    global game_over
    count = 0
    for i in range(1, 10):
        if str(i) in pos:
            break
        else:
            count += 1
    if count == 9:
        print('The game has ended in a tie.')
        game_over = True

wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
        [2, 5, 8], [0, 4, 8], [2, 4, 6]]

stop_all = False

while not stop_all:
    bot = input("Would you like to play 2-player or against a bot? (2/b) ").lower()
    pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    first = random.choice(['y', 'n'])

    display_board(pos)
    game_over = False
    while not game_over:

        if bot == '2':
            play_turn('X')
            play_turn('O')
            play_again()

        if bot == 'b':
            if first == 'y':
                play_turn('X')
                bot_play()
                play_again()
            if first == 'n':
                bot_play()
                play_turn('X')
                play_again()
