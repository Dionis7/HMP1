
import math

x1=int(input("Введите число для х1: "))
y1=int(input("Введите число для y1: "))
x2=int(input("Введите число для х2 : "))
y2=int(input("Введите число для y2 : "))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'Расстояние между точками А({x1}, {y1}) и В({x2}, {y2}) -> {distance}')