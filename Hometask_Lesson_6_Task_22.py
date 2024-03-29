# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа.
# n - кол-во элементов первого множества. т - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.
# 11 6 
# 2 4 6 8 10 12 10 8 6 4 2 
# 3 6 9 12 15 18 
# → 6 12

p = int(input()) # количество элементов первого множества
t = int(input()) # количество элементов второго множества

set1 = set()
for i in range(p):
    set1.add(int(input()))

set2 = set()
for i in range(t):
    set2.add(int(input()))

# находим пересечение множеств и выводим его в порядке возрастания
result = sorted(set1.intersection(set2))
for num in result:
    print(num)