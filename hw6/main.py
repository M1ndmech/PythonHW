import random
'''
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. 
Каждое число вводится с новой строки.

Ввод: 7 2 5 Вывод: 7 9 11 13 15
'''

a_input = int(input('Введите число - начало прогрессии:'))
d_input = int(input('Введите число - шаг прогрессии:'))
n_input = int(input('Введите количество членов прогрессии:'))

def progression (start, increment, steps):
    list = []
    for i in range (0, steps*increment, increment):
        list.append(start + i)
    return list

print (progression(a_input, d_input, n_input))

'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] 
Ввод: [7, 10]
Вывод: [1, 9, 13, 14, 19]
'''

def random_int_list (length, min, max):
    list = []
    for i in range (length):
        list.append(random.randint(min,max))
    return list

def get_indexes (list1, start_input, end_input) -> list:
    indexes = []
    for i in range(len(list1)):
        if list1[i] >= start_input and list1[i] <= end_input:
            indexes.append(i)
    return indexes

a_length = int(input('Введите длину списка:'))
a_start = int(input('Введите минимальное значение списка:'))
a_end = int(input('Введите максимальное значение списка:'))
a_list = random_int_list(a_length, a_start, a_end)

start_input = int(input('Введите начало диапазона:'))
end_input = int(input('Введите начало диапазона:'))

print (a_list)
print(get_indexes(a_list, start_input, end_input))

