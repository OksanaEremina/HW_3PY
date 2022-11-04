# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")

# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)
# lst = list(map(int, input("Ввести числа через пробел:\n").split()))
# sum_odd_index(lst)


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint


# number = int(input('Ввести размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# lst = list(map(float, input("Ввести вещественные числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# a = int(input('Ввести число: '))
# b = ''
# while a > 0:
#     b = str(a%2) + b
#     a = a // 2
# print(b)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Ввести размер числа Фибоначчи: '))
# if n < 0: n = n*-1
# f1 = f2 = 1
# list1 = [f1, f2]
# for i in range(2, n):
#     f1,f2 = f2, f1 + f2
#     list1.append(f2)
# print(list1)
# f1=f2=1
# for i in range(-n, 1):
#     f1,f2 = f2, f1 - f2
#     list1.insert(0, f2)
# print(list1)

