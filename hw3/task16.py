# Задача 16. Требуется вычислить, сколько раз встречается некоторое число result_number
# в массиве A[1..numbers]. Пользователь в первой строке вводит натуральное число numbers –
# количество элементов в массиве. В последующих строках записаны numbers целых чисел Ai.
# Последняя строка содержит число result_number

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

numbers = int(input('Введите количество элементов массива: '))
my_array = input('Введите через пробел элементы массива: ').split()
number_my_array = list(map(int, my_array))
if len(number_my_array) != numbers:
    print('Введено неверное количество элементов')
else:
    result_number = int(input('Введите число искомое число: '))
    count = 0
    for i in range(numbers):
        if number_my_array[i] == result_number:
            count = count + 1
    print(f'Число {result_number} встречается в списке {count} раз')
