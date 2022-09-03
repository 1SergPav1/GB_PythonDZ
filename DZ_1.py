# Задание_1

num_of_day = int(input("Введи номер дня недели: "))
if num_of_day in (6, 7):
    print('да')
else:
    print('нет')

# Задание_2

xyz = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
]

for i in xyz:
    morgan = not(i[0] or i[1] or i[2]) == ((not i[0]) and (not i[1]) and (not i[2]))
    print(morgan)


# Задание_3

x = int(input("Введи Х (не равное 0): "))
y = int(input("Введи Y (не равное 0): "))

if x == 0 or y == 0:
    print('Некорректный ввод!')
elif x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')

# Задание_4

num = int(input('Введи номер четверти: '))
if num not in (1, 2, 3, 4):
    print('Некорректный ввод')
elif num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0')

# Задание_5

import math

x1 = int(input("Введи координату Х точки А: "))
y1 = int(input("Введи координату Y точки А: "))
x2 = int(input("Введи координату Х точки В: "))
y2 = int(input("Введи координату Y точки В: "))

x = x2 - x1
y = y2 - y1
answer = math.sqrt(x**2 + y**2)
print('Расстояние между точками А и В = ', answer)


