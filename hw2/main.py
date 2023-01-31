import random
import math

'''
Задача №1:
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
'''

def random_int_list (length, min, max):
    list = []
    for i in range (length):
        list.append(random.randint(min,max))
    return list

def turn_coins_over (list):
    i = 0
    heads, tails = 0, 0
    while (i < len(list)):
        if list[i] == 0:
            heads += 1
        else:
            tails += 1
        i += 1
    if heads > tails:
        return (tails)
    else:
        return (heads)

coins_input = int(input("Введите количество монет на столе: "))
coins_list = random_int_list(coins_input, 0, 1)
print(coins_list)
print(turn_coins_over(coins_list))


'''
Задача №2:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Пример:
4 4 -> 2 2
5 6 -> 2 3
'''

def quadratic_equation (a, b, c):
    d = b ** 2 - 4 * a * c
    if (d < 0):
        return ("No answer")
    elif (d == 0):
        x_1 = -b / (2 * a)
        return (x_1, x_1)
    else:
        x_1 = (-b + math.sqrt(d))/(2 * a)
        x_2 = (-b - math.sqrt(d))/(2 * a)
        return (x_1, x_2)

s = int(input("Введите первую подсказку - сумму двух чисел: "))
p = int(input("Введите вторую подсказку - произведение двух чисел: "))

# x + y == s
# x * y == p
# x*(s - x) == p
# x^2 - s*x + p == 0

print (quadratic_equation (1, -s, p))


'''
Задача №3:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
'''

def power_list (number, limit):
    list = []
    i = 0
    n = 0
    for i in range (limit):
        n = number**i
        if n > limit:
            break
        else:
            list.append(n)
        i += 1
        
    return list

number_input = int(input("Введите число для построения ряда: "))
limit_input = int(input("Введите верхний предел ряда: "))

print (power_list(number_input, limit_input))