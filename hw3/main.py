import random
import math

'''
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X
Длина массива = 5 
Массив = 1 2 3 4 5 
Х = 3
-> 1
'''

def random_int_list (length, min, max):
    list = []
    for i in range (length):
        list.append(random.randint(min,max))
    return list

def count_number_in_values (list, number):
    counter = 0
    for item in list:
        if item == number:
            counter += 1
    return counter

length_input = int(input("Введите длину списка: "))
min_input = int(input("Введите минимальное значение списка: "))
max_input = int(input("Введите максимальное значение списка: "))
number_input = int(input("Введите искомое число: "))
list1 = random_int_list(length_input, min_input, max_input)
print (list1)
if count_number_in_values(list1, number_input) == 0:
    print (f'Число {number_input} в списке не найдено')
else:
    print (f'Количество вхождений числа {number_input} в списке - {count_number_in_values(list1, number_input)}')


'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X
Длина массива = 5 
Массив = 1 2 3 4 5 
X = 6
-> 5
'''
def lookup_closest_value (list, number):
    closest = list [0]
    for i in range (1, len (list)):
        if (abs(list [i] - number)) < (abs(closest - number)):
            closest = list [i]
    return closest

length_input_2 = int(input("Введите длину списка: "))
min_input_2 = int(input("Введите минимальное значение списка: "))
max_input_2 = int(input("Введите максимальное значение списка: "))
number_input_2 = int(input("Введите искомое число: "))
list2 = random_int_list(length_input_2, min_input_2, max_input_2)
print (list2)
if (lookup_closest_value(list2, number_input_2) == number_input_2):
    print (f'В списке присутствует искомое число {lookup_closest_value(list2, number_input_2)}')
else:
    print (f'Ближайшее к числу {number_input_2} число в списке равно {lookup_closest_value(list2, number_input_2)}')


'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так: 
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 

А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
Пример: ввод - "ноутбук", вывод - 12
'''

def scrabble (word):
    eng_1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
    eng_2 = dict.fromkeys(['D', 'G'], 2)
    eng_3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3) 
    eng_4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
    eng_5 = dict.fromkeys(['K'], 5)
    eng_8 = dict.fromkeys(['J', 'X'], 8) 
    eng_10 = dict.fromkeys(['Q', 'Z'], 10)
    dict_eng = eng_1 | eng_2 | eng_3 | eng_4 | eng_5 | eng_8 | eng_10

    rus_1 = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
    rus_2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
    rus_3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3) 
    rus_4 = dict.fromkeys(['Й', 'Ы'], 4)
    rus_5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
    rus_8 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8) 
    rus_10 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
    dict_rus = rus_1 | rus_2 | rus_3 | rus_4 | rus_5 | rus_8 | rus_10 
        
    list_scr = list(word.upper())
    score = 0
    if list_scr[0] in list(dict_rus):
        for item in list_scr:
            score += int(dict_rus.get(item))
        return score
    for item in list_scr:
        score += int(dict_eng.get(item))
    return score

scrabble_word = input("Введите слово для игры: ")
print (scrabble(scrabble_word))