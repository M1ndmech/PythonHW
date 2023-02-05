'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
Пользователь вводит 2 числа. 
n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.

m, n = 11 6 
input m = 2 4 6 8 10 12 10 8 6 4 2 
input n = 3 6 9 12 15 18 

output = 6 12
'''

def input_int_list (length, message, comment = ""):
    list = []
    for i in range (length):
        input_symbol = input(f'Введите {message} {i+1}{comment}: ')
        list.append(int(input_symbol))
    return list

m_n_input = input_int_list(2, 'длину списка')
m_list = set(input_int_list (m_n_input[0], 'элемент', " первого множества"))
n_list = set(input_int_list (m_n_input[1], 'элемент', " второго множества"))
set1 = list(m_list.intersection(n_list))
set1.sort()
print(set1)

'''
В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. 
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. 
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.

4 -> 1 2 3 4 
9

'''

def gen_ascending_list (length):
    list = []
    for i in range (length):
        list.append(i+1)
    return list

# вариант 1 - суммирует количество выбранного места и двух соседних

def sum_row_part(number, input_list, length = 3):
    sum = 0
    selection_list = []
    for i in range (length):
        selection_list.append(number - i)
    if number == len (input_list):
        selection_list [0] = 0
    for item in selection_list:
        sum += input_list[item]
    return sum

shrub_list_input = int(input('Введите количество кустов на грядке:'))
shrub_input = int(input('Введите номер искомого куста:'))
shrubs = gen_ascending_list(shrub_list_input)
print(shrubs)
print(f'Количество собранных ягод при выборе {shrub_input} куста = {sum_row_part(shrub_input, shrubs)}')

# вариант 2 - максимальное значение трех соседних элементов

def sum_max_part(input_list, length = 3):
    max_sum = 0
    for i in range (0, len(input_list)):
        if sum(input_list[i:(i+length)]) > max_sum:
            max_sum = sum(input_list[i:(i+length)])
    return max_sum

print(f'Максимальное количество собранных ягод за 1 заход = {sum_max_part(shrubs)}')