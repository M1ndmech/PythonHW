'''
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵) 
A = 2; B = 3 -> 8
'''
def recursive_power (number, power):
    if power == 0:
        return 1
    else:
        return number * recursive_power(number, power - 1)


input_number = int(input('Введите число для возведения в степень:'))
input_power = int(input('Введите степень:'))
print(recursive_power(input_number, input_power))

'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
'''

def recursive_sum (number_1, number_2):
    if number_2 == 0:
        return number_1
    else:
        return recursive_sum(number_1 + 1, number_2 - 1)

number_1 = int(input('Введите число 1 для суммирования:'))
number_2 = int(input('Введите число 2 для суммирования:'))
print(recursive_sum(number_1, number_2))