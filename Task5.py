'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def fibonacci(number):
    for n in range(number+1):
        if n == 0:
            lst_1.append(0)
        elif n == 1:
            lst_1.append(1)
        else:
            lst_1.append(lst_1[n-1] + lst_1[n-2])
    fib_lst = [(-1)**(n+1)*lst_1[n] for n in range(len(lst_1)-1, 0, -1)]
    return fib_lst + lst_1


num = int(input('Введите количество элеменктов списка: '))
lst_1= []
print('Числа Фибоначчи: ', fibonacci(num))