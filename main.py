# HW 4
# Make a programm which displays palindrome words => 'kak' - 'kak'
# 1. The programm needs to get input from user
# 2. The programm needs to turn over words backwordly using ::-1
# 3. The indexes of the letters in the word need to be the same when letters are backworded e.g letter 0
#     has to equal to letter in index -1, and so on
# 4. Output the result
#
# while True: # creating infinite progam
#     letter_to_check = [] #initializing the list for letters to check if it is palindrome
#     word_to_check = input('Enter your word to check if it is Palindrome: ')
#
#     if word_to_check.lower() == 'stop': # check if the user wants to stop the programm
#         print('You have stop the programm. God bye')
#         break
#
#     for letter in word_to_check:    # adding letters to the list using for loop
#         letter_to_check.append(letter)
#
#     backward = letter_to_check[::-1] # backwarding the words in the list
#
#     if letter_to_check == backward:
#         print(f'Entered word: {word_to_check} is Palindrome.')
#     else:
#         print(f'Entered word: {word_to_check} is not Palindrome')
#
# Дополнительные ДЗ упр. 5 здаем бутылки
# bottles 1ltr > lower == 010$ deposit
# bottles 1ltr < == 0.25$ deposit
# Task: need get input of bottles amount from user and their size on the screen we have to see:
# the totall profit of giving back bottles
# 1. Запрашиваем у юзера виды бутылок 2 инпута Making 2 inputs
# 2. Сравниваем через иф какая бутылка относиться к какому размеру
# 3. В зависимости от количества умножаем цену на количество бутылок
# 4. if user has 2 types of bottles summing the amount
# 5. writing the result in details
# while True:
#     big_bottles = int(input('How many big bottles you have? Enter amount or "0" if you do not have'))
#     small_bottles = int(input('How many small bottles you have? Enter amount or "0" if you do not have'))
#
#     if big_bottles < 0 or small_bottles < 0: # проверка вводит ли пользователь правильное значение а не -
#         print('Введите числа 0 или выше')
#     else:
#         sum_big = big_bottles * 0.25
#         sum_small = small_bottles * 0.10
#         total = sum_big + sum_small
#         print(f'Ваша прибыль от здачи бутылок ${ total:.2f}')
#
#     stop = input('Do you want to stop program? or continue. Press "Yes" to stop and "No" to continue').lower()
#     if stop == 'yes':
#         print('You stop the program. Good Bye')
#         break
#     else:
#         continue
#
# Дополнительное ДЗ упражнение 6
#
# Задание 6: Налоги и чаевые
#
# Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане.
# После этого должен быть произведён расчёт налога и чаевых для официанта.
# Вы можете использовать принятую в вашем регионе налоговую ставку для подсчёта суммы сборов.
# В качестве чаевых мы оставим 18% от стоимости заказа без учёта налога.
#
# На выходе программа должна отобразить:
#
# Сумму налога.
# Сумму чаевых.
# Общую сумму (включающую налог и чаевые).
# Форматируйте вывод таким образом, чтобы все числа отображались с двумя знаками после запятой.
#
# amount = int(input('Enter amount of the bill: '))
# tax = (amount / 100) * 12
# tip = (amount / 100) * 18
# total = amount + tax + tip
#
# print(f'''
# Your total bil: ${total:.2f}
# Tax: ${tax:.2f}
# Tip: ${tip:.2f}
# ''')
#
# Задание 7: Сумма первых n положительных чисел
#
# Напишите программу, запрашивающую у пользователя число и подсчитывающую сумму
# натуральных положительных чисел от 1 до введённого пользователем значения.
# Сумма первых n положительных чисел может быть рассчитана по формуле:
#
# sum = (n(n+1)) / 2
#
# n = int(input('Enter the positive number: '))
#
# sum = (n * (n+1)) // 2
#
# print(f'amount of first and positive numbers is: {sum}')
#
# Дополнительное задание 8.Сувениры и безделушки
# 1.Ask from user the kg of each present
# 2.Write totall kg of each item
#
# souvenirs = int(input('How many pc of Sovenir you need?: '))
# bezdelushki = int(input('How many Bezdelushki you need?: '))
#
# print(f'''
# Your souvenirs are: {souvenirs * 0.072:.3f}kg
# Your bezdelushki are: {bezdelushki * 0.112:.3f}kg
# ''')
#
