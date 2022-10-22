'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

from random import randint

def arr_():
    for i in range(size_):
        lst_.append(randint(0, 10))
    print(lst_)

def summa_(lst_):
    sum_ = sum(lst_[i] for i in range(0, len(lst_), 2))
    print(f"Сумма нечетных элементов: \n {sum_}")

size_ = int(input('Введите количество элеменктов списка: '))
lst_ = []
arr_()
summa_(lst_)