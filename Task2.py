'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
from random import randint

def arr_():
    for i in range(size_):
        lst_.append(randint(0, 10))
    print(lst_)

def mass(lst_):
    for i in range((len(lst_)+1) // 2):
        prod_.append(lst_[i] * lst_[-1 + (-i)])
    print(prod_)

size_ = int(input('Введите количество элеменктов списка: '))
lst_ = []
prod_ = []
arr_()
mass(lst_)
