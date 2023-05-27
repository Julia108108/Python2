# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('Введите число: '))
stepen = 0

while 2 ** stepen < number:
    print(2 ** stepen)
    stepen = stepen + 1
    