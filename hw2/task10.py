# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

coins = int(input('Введите количество монет: '))
orel = reshka = 0

for i in range(coins):
    x = int(input('Введите последовательно наименования монет, где 0 - это орёл, а 1 - это решка: '))
    if x == 1:
        orel = orel + 1
    else:
        reshka = reshka + 1 
        
if orel < reshka:
    print(f'Переверните {orel} монет/у')
elif orel == reshka:
    print(f'Количество орлов и решек одинаковое: {orel} штук')
else:
    print(f'Переверните такое количество монет: {reshka}')
          