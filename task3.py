# В некоторой школе решили набрать три новых математических класса и 
# оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество 
# учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input("Количество учащихся в 1 класcе: "))
b = int(input("Количество учащихся в 2 классе: "))
c = int(input("Количество учащихся в 3 классе: "))
desk = (a + b + c) // 2 + (a + b + c) % 2
print (f"Минимальное количество парт: {desk}")

# 2
firstClass = int(input("сколько учеников в первом классе: "))
secondClass = int(input("сколько учеников во втором классе: "))
thirdClass = int(input("сколько учеников в третьем классе: "))
import math
desks = (math.ceil(firstClass/2)) + (math.ceil(secondClass/2)) + (math.ceil(thirdClass/2))
print("сколько необходимо парт: ",desks)

#3
class1 = int(input('Класс А:\n'))
class2 = int(input('Класс Б:\n'))
class3 = int(input('Класс В:\n'))

partSum = (class1 // 2 + class1 % 2) + (class2 // 2 + class2 % 2) + (class3 // 2 + class3 % 2)

print(f'Для учеников потребуется {partSum} парт')