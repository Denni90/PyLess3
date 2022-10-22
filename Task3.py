'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

def  float_mass(number):
    number2 = [round(n % 1, 2) for n in number if n % 1 != 0]
    return max(number2) - min(number2)


number = [1.1, 1.2, 3.1, 5, 10.01]
print(number)
print(float_mass(number))