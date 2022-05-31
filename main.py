def hello():
    print('--------------------')
    print('------Weclome-------')
    print('----to the game:----')
    print('----Tic-Tac-Toe-----')
    print('--------------------')
    print('-INSTRUCTION:-------')
    print('-input format: x y--')
    print('-x - line number----')
    print('-y - column number--')
    print('--------------------')

hello()

field = [[" "] * 3 for i in range (3)]

def showfield():
    print()
    print(f'   | 0 | 1 | 2 |')
    print('-----------------')
    for i, row in enumerate(field):
        row2 = f" {i} | {' | '.join(row)} | "
        print(row2)
        print('-----------------')
    print()

def xy():
    while True:
        num = input('Enter x and y: ').split()

        if len(num) != 2:
            print('Two values must be entered.')
            continue

        x, y = num

        if not(x.isdigit()) or not(y.isdigit()):
            print('Only numbers must be entered.')
            continue

        if not(x.isalnum()) or not(y.isalnum()):
            print('Only numbers must be entered.')
            continue

        x, y, = int(x), int(y)

        if x not in range(0, 3):
            print('X must not be greater than 2 and less than 0.')
            continue

        if y not in range(0, 3):
            print('Y must not be greater than 2 and less than 0.')
            continue

        if field[x][y] != ' ':
            print('Cell must be free.')
            continue

        return x, y

def win():
    for  i in range(3):
        result = []
        for j in range(3):
            result.append(field[i][j])
        if result == ['X', 'X', 'X']:
            return True
        elif result == ['0', '0', '0']:
            return True

    for  i in range(3):
        result = []
        for j in range(3):
            result.append(field[j][i])
        if result == ['X', 'X', 'X']:
            return True
        elif result == ['0', '0', '0']:
            return True

    result = []
    for i in range(3):
        result.append(field[i][i])
    if result == ['X', 'X', 'X']:
        return True
    elif result == ['0', '0', '0']:
        return True

    result = []
    for i in range(3):
        result.append(field[i][2-i])
    if result == ['X', 'X', 'X']:
        return True
    elif result == ['0', '0', '0']:
        return True

    return False

move = 0
while True:
    move += 1

    showfield()

    if move % 2 == 1:
        print('Player #1 (X) moving now!')
    else:
        print('Player #2 (0) moving now!')

    x, y = xy()

    if move % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if win():
        showfield()
        print('Number of moves:', move)
        if move % 2 == 1:
            print('Player #1 (X) win!')
        else:
            print('Player #2 (0) win!')
        break

    if move == 9:
        showfield()
        print('Draw!')
        break
