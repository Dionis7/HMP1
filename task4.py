a = int(input("Введите любую цифру от 1 до 4 : "))

match a:
    case 1:
        print("x>0, y>0")
    case 2:
        print("x>0, y<0")
    case 3:
        print("x<0, y<0")
    case 4:
        print("x<0, y>0")
    case _:
        print("Ошибка")