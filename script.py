# Begin
from random import randint  # import random
print("welcome to game ")  # welcome a gamer
print("перед тобой поле для игры ")
print()


def player_input():  # function that verify type and range
    while True:
        # принять координаты
        string_for_game = input("Введите номер строки: ")
        column_for_game = input("Введите номер колонки: ")

        # если не цифры:
        #     continue
        if string_for_game.isdigit() == False or column_for_game.isdigit() == False:
            print()
            print("Вы должны ввести цифры")
            continue

        # преобразовать в числовой тип
        string_for_game = int(string_for_game)
        column_for_game = int(column_for_game)

        # если неправильные числа:
        #     continue
        if string_for_game <= 0 or string_for_game >= 4 or column_for_game <= 0 or column_for_game >= 4:
            print()
            print("Полажуйста, введите цифры от 1 до 3")
            continue

        return string_for_game, column_for_game  # return the coordinate


def field_for_function():  # function that create the field, verify contents of coordinate

    first_string = [" ", 1, 2, 3]  # the four list for field
    second_string = [1, "*", "*", "*"]
    third_string = [2, "*", "*", "*"]
    fourth_string = [3, "*", "*", "*"]
    tuple_string = (first_string, second_string, third_string, fourth_string)  # the tuple of the string

    for j in range(4):  # inference field for the gamer
        print(*tuple_string[j])
    print()

    for i in range(3):  # a cycle for fill of the contents of coordinate
        print("Пожалуйста введите цифры от 1 до 3")
        print()

        a = player_input()  # take data of gamer adn verify
        string_for_game, column_for_game = a[0], a[1]  # assign string and column

        while tuple_string[string_for_game][column_for_game] == "0" or tuple_string[string_for_game][column_for_game] == "x":  # verify zero and x in coordinates
            print("На этих координатах стоит 0 или вы уже ввели x, ввведите другие данные")

            a = player_input()  # take data of gamer adn verify
            string_for_game, column_for_game = a[0], a[1]  # assign string and column
        tuple_string[string_for_game][column_for_game] = "x"  # assign x

        a_random_string = randint(1, 3)  # assign string and column random numbers
        a_random_column = randint(1, 3)

        while tuple_string[a_random_string][a_random_column] == "x" or tuple_string[a_random_string][a_random_column] == "0":  # verify zero and x in coordinates
            a_random_string = randint(1, 3)
            a_random_column = randint(1, 3)
        tuple_string[a_random_string][a_random_column] = "0"  # assign x

        for j in range(4):  # inference field with contents
            print(*tuple_string[j])
    return tuple_string


def counting_of_the_game(counting_tuple):  # the checking function is winner

    counting_1 = None  # variable for check winner

    for i in range(4):  # cycle for check string and column

        counting_x = 0  # count x
        counting_0 = 0  # count x
        for j in range(4):  # check who is winner horizontal, if in string three x or 0
            if counting_tuple[i][j] == "x":
                counting_x += 1
            elif counting_tuple[i][j] == "0":
                counting_0 += 1
        if counting_x == 3:
            counting_1 = 1  # if winner x
        elif counting_0 == 3:
            counting_1 = 2  # if winner 0

        counting_x = 0
        counting_0 = 0
        for j in range(4):  # check who is winner vertical, if in string three x or 0
            if counting_tuple[j][i] == "x":
                counting_x += 1
            elif counting_tuple[j][i] == "0":
                counting_0 += 1
        if counting_x == 3:
            counting_1 = 1  # if winner x
        elif counting_0 == 3:
            counting_1 = 2  # if winner 0
        counting_x = 0
        counting_0 = 0

        b = 1
        for j in range(3):  # check who is winner diagonal, if in string three x or 0
            if counting_tuple[b][j+1] == "x":
                counting_x += 1
            elif counting_tuple[b][j+1] == "0":
                counting_0 += 1
            b += 1
        if counting_x == 3:
            counting_1 = 1  # if winner x
        elif counting_0 == 3:
            counting_1 = 2  # if winner 0
        counting_x = 0
        counting_0 = 0

        b = 1
        a = 3
        for j in range(3):  # check who is winner diagonal in the opposite direction, if in string three x or 0
            if counting_tuple[b][a] == "x":
                counting_x += 1
            elif counting_tuple[b][a] == "0":
                counting_0 += 1
            b += 1
            a -= 1
        if counting_x == 3:
            counting_1 = 1
        elif counting_0 == 3:
            counting_1 = 2

    if counting_1 == 1:
        print("Игрок победил")
    elif counting_1 == 2:
        print("Победил компьютер")
    else:
        print("Ничья")
    return counting_1


counting_of_the_game(field_for_function())
input()  # ввод чтобы из консоли резко не выходил

