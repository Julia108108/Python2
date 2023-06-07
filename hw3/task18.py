# Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

numbers = int(input('Введите количество элементов массива: '))
my_array = input('Введите через пробел элементы массива: ').split()
number_my_array = list(map(int, my_array))
if len(number_my_array) != numbers:
    print('Введено неверное количество элементов')
else:
    result_number = int(input('Введите число, с которым необходимо сравнивать: '))
    min = result_number - number_my_array[0]
    index = 0
    for i in range(1, numbers):
        count = result_number - number_my_array[i]
        if count < min:
            min = count
            index = i
    print(f'Самое близкое число к числу {result_number}: {number_my_array[index]} ')
