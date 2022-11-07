# homework = True
# while homework:
#     homework = (input("Введите номер задачи (1, 2, 3, 4), для выхода введите 'exit': "))
#     if homework == 'exit':
#         homework = not homework
#     elif homework == '1':
#         finding_multiplier(N)
#     elif homework == '2':
#         ice_cream()
#     elif homework == '3':
#         pi()
#     elif homework == '4':
#         polynomial()
        

# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

N = int(input("Ищем простые множители числа: "))

def finding_multiplier(N):
    i = list()
    j = 2
    while j <= N:
        if (N % j) == 0:
            i.append(j)
            N = N / j
        else:
            j += 1
    return i
print(f"Число {N} состоит из следующих простых множителей: {finding_multiplier(N)}")

finding_multiplier(N)

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

def ice_cream ():

    file = open("ice_cream.txt", "r", encoding='utf-8')
    data = file.readlines()
    file.close()
    assortment = set(data[0].replace("\n", "").split(", "))
    on_stock = set(data[1].replace("\n", "").split(", "))
    out_of_stock = assortment.difference(on_stock)
    print (f'Ассортимент мороженного: {assortment}')
    print (f'Мороженое на остатках: {on_stock}')
    print (f'Закончилось мороженное: {str(out_of_stock)}')

ice_cream ()

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.3 -> 3.142
# 5 -> 3.14159

def pi():
    import math
    prec = int(input('Введитете количество знаков после запятой: '))
    print(round(math.pi,prec))
pi()

# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x2. 3x^2 + x + 8Результат: 8x^2 + 4x + 8

def polynomial():
    print ('С задачей №4 справиться пока не удалось')
polynomial ()