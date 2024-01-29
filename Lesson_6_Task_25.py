# Задача №25. Напишите программу, которая на вход принимает строку, и отслеживает, сколько раз каждый символ 
# уже встречался. Количество повторов  добавляется к символам с помощью постфикса формата _n
# Input: aaabcaadcdd
# Output: aa_1a_2bca_3a_4dc_1d_1d_2
stroka = input().split()
res = {}

for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}', end=', ')
    else:
        print(i, end=' ')    
        
    res[i]= res.get(i, 0) + 1