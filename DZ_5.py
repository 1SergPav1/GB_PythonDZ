# Задание № 1
# str = 'абв гд5вап'
#
# res = list(filter(lambda x: 'абв' not in x, str.split()))
#
# print(''.join(res))

# Задание № 2

# import random
# candies = 200
# count = 1
# print('Всего', candies, 'конфет! Игра началась')
#
# while candies > 0:
#     if count % 2 != 0:
#         move = int(input('Твой ход: '))
#         if 0 < move < 29:
#             candies -= move
#             count += 1
#             if candies == 0:
#                 print('Ты победил!')
#             else:
#                 print('Осталось', candies, 'конфет')
#         else:
#             print('Ты можешь взять максимум 28 кофет за один ход')
#             print('Осталось', candies, 'конфет')
#             continue
#     else:
#         if candies > 28:
#             bot_move = random.randint(1, 28)
#             print('Ходит бот: ', bot_move)
#             candies -= bot_move
#             count += 1
#             print('Осталось', candies, 'конфет')
#         else:
#             bot_move = candies
#             print('Ходит бот: ', bot_move)
#             candies -= bot_move
#             print('Бот победил')

# Задание № 3

# my_board = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
#
# board_dict = {1: '00', 2: '01', 3: '02', 4: '10', 5: '11', 6: '12', 7: '20', 8: '21', 9: '22'}
# win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
#
#
# def show_board(board):
#     for row in board:
#         for elem in row:
#             print(elem, end=' ')
#         print()
#
#
# def take_move(player):
#     while True:
#         move = input('\nВаш ход ' + player + ': ')
#         try:
#             move = int(move)
#         except:
#             print('Некорректный ввод')
#             continue
#         if int(move) in range(1, 10):
#             if str(my_board[int(board_dict[move][0])][int(board_dict[move][1])]) not in 'XO':
#                 my_board[int(board_dict[move][0])][int(board_dict[move][1])] = player
#                 break
#
#
# # take_move('X')
# # show_board(my_board)
#
#
# def check_win(board):
#     for i in win_list:
#         if board[int(board_dict[i[0]][0])][int(board_dict[i[0]][1])] == board[int(board_dict[i[1]][0])][
#             int(board_dict[i[1]][1])] == board[int(board_dict[i[2]][0])][int(board_dict[i[2]][1])]:
#             return board[int(board_dict[i[0]][0])][int(board_dict[i[0]][1])]
#     return False
#
#
# def main(board):
#     count = 0
#     win = False
#     while not win:
#         show_board(my_board)
#         if count % 2 == 0:
#             take_move('X')
#         else:
#             take_move('O')
#         count += 1
#         if count > 4:
#             check = check_win(my_board)
#             if check:
#                 print(check, 'победил')
#                 win = True
#                 break
#     show_board(my_board)
#
#
# main(my_board)

# Задание № 4

# data_file = open('DZ_5_4.1.txt', 'r')
# result_file1 = open('DZ_5_4.2.txt', 'r+')
# result_file2 = open('DZ_5_4.3.txt', 'w')
# result = ''
# count = 1
# i = 0
#
# data = data_file.read()
# print(data)
# while i < len(data) - 1:
#     if data[i] != data[i + 1]:
#         result += str(count) + data[i]
#         count = 1
#         i += 1
#     else:
#         count += 1
#         i += 1
# result += str(count) + data[i]
#
# result_file1.write(result)
# result_file1.close()
#
# result_file1 = open('DZ_5_4.2.txt', 'r+')
# data_decode = result_file1.read()
# print(data_decode)
# result_decode = ''
# count = ''
#
# for i in data_decode:
#     if i.isdigit():
#         count += i
#     else:
#         result_decode += i * int(count)
#         count = ''
# result_file2.write(result_decode)


