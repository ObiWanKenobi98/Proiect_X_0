'''Iulian Nicula'''

def check_game_state(value):
    for i in range(1, 4, 1):
        no_X = 0
        no_0 = 0
        for j in range(1, 4, 1):
            if value[i][j] == 'X':
                no_X += 1
            elif value[i][j] == '0':
                no_0 += 1
        if no_X == 3:
            print("Game over! X has won!")
            return True
        elif no_0 == 3:
            print("Game over! 0 has won!")
            return True
        no_X = 0
        no_0 = 0
        for j in range(1, 4, 1):
            if value[j][i] == 'X':
                no_X += 1
            elif value[j][i] == '0':
                no_0 += 1
        if no_X == 3:
            print("Game over! X has won!")
            return True
        elif no_0 == 3:
            print("Game over! 0 has won!")
            return True

    for i in range(1, 4, 1):
        no_X = 0
        no_0 = 0
        if value[i][i] == 'X':
            no_X += 1
        elif value[i][i] == '0':
            no_0 += 1
        if no_X == 3:
            print("Game over! X has won!")
            return True
        elif no_0 == 3:
            print("Game over! 0 has won!")
            return True

    for i in range(1, 4, 1):
        no_X = 0
        no_0 = 0
        if value[i][3 - i + 1] == 'X':
            no_X += 1
        elif value[i][3 - i + 1] == '0':
            no_0 += 1
        if no_X == 3:
            print("Game over! X has won!")
            return True
        elif no_0 == 3:
            print("Game over! 0 has won!")
            return True
    return False


def print_game_state(value):
    for i in range(1, 4, 1):
        str = ""
        for j in range(1, 4, 1):
            str += value[i][j] + " "
        print(str)


def get_next_moves(value):
    txt = ""
    for i in range(1, 4, 1):
        for j in range(1, 4, 1):
            if value[i][j] == '-':
                txt = txt + "(" + str(i) + ", " + str(j) + "); "
    return txt


turn = 0
max_turns = 9
init_message = "Turn number "
def_message = "choose your next move; available: "
value = [['-' for i in range(1, 5, 1)] for j in range(1, 5, 1)]
game_over = False

for i in range(1, 4, 1):
    for j in range(1, 4, 1):
        value[i][j] = '-'

while (turn < max_turns) and (game_over is False):
    print(init_message + str(turn))
    txt = get_next_moves(value)
    if turn % 2 == 0:
        print("X turn: " + def_message + txt)
        x = int(input("X coordinate:"))
        y = int(input("Y coordinate:"))
        print(x, y)
        value[x][y] = 'X'
    else:
        print("0 turn: " + def_message + txt)
        x = int(input("X coordinate:"))
        y = int(input("Y coordinate:"))
        print(x, y)
        value[x][y] = '0'
    game_over = check_game_state(value)
    print_game_state(value)
    turn += 1

if game_over is False:
    print("Game over! It's a tie!")


