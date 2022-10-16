# Задание № 1

# st = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
#
# lst = st.split('О')
# lst = list(filter(lambda x: 'Р' in x, lst))
# try:
#     print(len(max(lst)))
# except:
#     print('Решек нет')

# Задание № 2

# # задание № 3 из ДЗ 2
# # Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# # старое решение
# # num = int(input('Введи число: '))
# # my_dict = {n: (1 + 1 / n) ** n for n in range(1, num + 1)}
# # print(my_dict)
# # print(sum(my_dict.values()))
#
# # новое решение
# num = int(input('Введи число: '))
# num_list = map((lambda x: (1 + 1 / x) ** x), range(1, num + 1))
# print(sum(num_list))

