# # Задание_1
#
# sum = 0
# num = input('Введи число: ')
# for n in num:
#     if n in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
#         sum += int(n)
# print('Cумма цифр числа: ', sum)
#
# # Задание_2
#
# res = 1
# res_list = []
# num = int(input('Введи число: '))
#
# for i in range(1, num + 1):
#     res *= i
#     res_list.append(res)
# print(res_list)
#
# # Задание_3
#
# num = int(input('Введи число: '))
# my_dict = {n: (1 + 1 / n) ** n for n in range(1, num + 1)}
# print(my_dict)
# print(sum(my_dict.values()))
#
# # Задание_4
#
# num_list = []
# result = 1
# file = open('DZ2_file.txt', 'r')
#
# num = int(input('Введи число: '))
#
# for _ in range(-num, num + 1):
#     num_list.append(_)
# print(num_list)
#
# for line in file:
#     result *= num_list[int(line)]
# print(result)
#
# # Задание_5
#
# import random
#
# num_list = []
# result = 1
# file = open('DZ2_file.txt', 'r')
#
# num = int(input('Введи число: '))
#
# for _ in range(-num, num + 1):
#     num_list.append(_)
# random.shuffle(num_list)
# print(num_list)
#
# for line in file:
#     result *= num_list[int(line)]
# print(result)
