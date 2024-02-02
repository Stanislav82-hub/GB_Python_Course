# Задача №31. Последовательностью Фибоначчи называется последовательность чисел а0, а1, а n, где a = 0, a, = 1,
# a = 2K1 + ax-2 (K> 1). Требуется найти N-e число Фибоначчи
# Input: 7
# Output: 8
def f(n):
    if n == 0 or n ==1:
        return 1
    return f(n-1) + f(n-2)

n = int(input('Please give me a number: '))

print(f(n - 2))