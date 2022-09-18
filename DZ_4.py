# # Задание №1

# import math
# def pi_acc(acc):
#     print(f'{math.pi:.{acc}f}')
#
# d = int(input('Введи точность вывода (количество знаков после точки): '))
#
# pi_acc(d)

# # Задание №2
#
# num = int(input('введи число: '))
# simple_nums_list = []
# simple = 2
# while num > 1:
#     if num % simple == 0:
#         simple_nums_list.append(simple)
#         num /= simple
#     else:
#         simple += 1
# print(simple_nums_list)

# # Задание №3
# import random
#
# num = random.choice(range(10))
# my_list = [random.randint(0, 10) for i in range(15)]
# print(my_list)
# result_list = list(set(my_list))
# print(result_list)

# # Задание №4
# import random
#
# coef_list = []
# poly = ''
#
# k = int(input('введи степень многочлена: '))
# for _ in range(k + 1):
#     coef_list.append(random.randint(0, 100))
#
# poly_dict = {x: y for x, y in zip(reversed(range(0, k + 1)),  coef_list)}
#
# for key in poly_dict:
#     if poly_dict[key] == 0:
#         continue
#     elif key > 1:
#         poly += f'{poly_dict[key]}x^{key} + '
#     elif key == 1:
#         poly += f'{poly_dict[key]}x + '
#     else:
#         poly += f'{poly_dict[key]} = 0'
#
# file = open('DZ_4_4_file.txt', 'w')
# file.write(poly)
# file.close()

# # Задание №5
# file1 = open('DZ_4_5.1.txt', 'r')
# file2 = open('DZ_4_5.2.txt', 'r')
# result_file = open('DZ_4_5.3.txt', 'w')
# poly1_args = []
# poly2_args = []
# poly = ''
#
# for line in file1:
#     x = line.replace('x', ' ')
#     poly1 = x.split(' ')
#     for i in poly1:
#         try:
#             poly1_args.append(int(i))
#         except ValueError:
#             pass
# print(poly1_args)
#
# for line in file2:
#     x = line.replace('x', ' ')
#     poly2 = x.split(' ')
#     for i in poly2:
#         try:
#             poly2_args.append(int(i))
#         except ValueError:
#             pass
# print(poly2_args)
#
# result_args = list(map(sum, zip(poly1_args, poly2_args)))
# print(result_args)
#
# result_poly = {x: y for x, y in zip(reversed(range(0, len(result_args) - 1)), result_args)}
# for key in result_poly:
#     if result_poly[key] == 0:
#         continue
#     elif key > 1:
#         poly += f'{result_poly[key]}x^{key} + '
#     elif key == 1:
#         poly += f'{result_poly[key]}x + '
#     else:
#         poly += f'{result_poly[key]} = 0'
#
# result_file.write(poly)
# result_file.close()
