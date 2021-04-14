# Печатаем название и правила игры
def greet():
    print("Игра крестики и нолики")
    print("")
    print("Формат ввода: х пробел у")
    print("где х - номер строки а y - номер столбца")

# Храним значения и печатаем поле для игры
def show():
    print()
    print("    | 0 | 1 | 2 |")
    print("-----------------")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("-----------------")
    print()

# Просим игрока сделать свой ход, проверяем введенные данные на занятость клетки и попадание в игровое поле0
def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
# проверяем победу
def check_win():
        win_cord = (((0,0),(0,1), (0,2)),((1,0),(1,1), (1,2)),((2,0),(2,1), (2,2)),
                    ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)),((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)),((0, 2), (1, 2), (2, 2)))
        for cord in win_cord:
            symbols = []
            for c in cord:
                    symbols.append(field[c[0]][c[1]])
            if symbols == ["X","X","X"]:
                print("Выиграл Х")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл 0")
                return True
        return False

#Игровой цикл
greet()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x,y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break

    if count ==9:
        print("Ничья")
        break