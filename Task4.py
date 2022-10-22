'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

def int_from_bin(number):
    b = ''
    while number > 0:
        b = str(number % 2) + b
        number //= 2
    return b

num = int(input("Введите число: "))
print(f"Следовательно:\n {num} -> {int_from_bin(num)}")