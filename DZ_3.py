# Задание_1

# sum_values = 0
#
# value_list = []
# while True:
#     num = input('Введи число - элемент списка (stop, чтобы закончить ввод): ')
#     if num == 'stop':
#         break
#     else:
#         value_list.append(int(num))
#         continue
#
# my_dict = {n: value_list[n] for n in range(len(value_list))}
# print(my_dict.values())
#
# for key in my_dict:
#     if key % 2 != 0:
#         sum_values += my_dict[key]
# print(sum_values)

# Задание_2

# my_list = [2, 3, 4, 5, 6]
# result_list = []
#
# new_list = my_list.copy()
# new_list.reverse()
#
# for i in range(len(my_list)):
#         result_list.append(my_list[i] * new_list[i])
# print(set(result_list))

# Задание_3

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
#
# for _ in range(len(my_list)):
#     my_list[_] %= 1
#
# for _ in my_list:
#     if _ == 0:
#         my_list.remove(0)
#
# print(f'{(max(my_list) - min(my_list)):.2f}')

# Задание_4

# num = int(input('Введи число: '))
# result = ''
#
# while num > 0:
#     result = str(num % 2) + result
#     num = num // 2
#
# print(result)

# Задание_5

# fib1 = 1
# fib2 = 1
# nfib1 = 1
# nfib2 = -1
#
# i = 0
# fib_list = [0, 1]
# negafib_list = [1, -1]
#
# n = int(input('Введи число: '))
#
# while i < n - 2:
#     sum = fib1 + fib2
#     fib_list.append(sum)
#     fib1 = fib2
#     fib2 = sum
#     res = nfib1 - nfib2
#     negafib_list.append(res)
#     nfib1 = nfib2
#     nfib2 = res
#     i += 1
#
# negafib_list.reverse()
# negafib_list.extend(fib_list)
# print(negafib_list)
