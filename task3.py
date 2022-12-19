x = int(input("Введите целое число координат x : "))
y = int(input("Введите целое число координаты y : "))

if x == 0 and y == 0:
    print('Ошибка')
elif x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)