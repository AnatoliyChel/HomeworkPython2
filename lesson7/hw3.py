"""Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
 которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
  Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint


def median(numbers):
    med = numbers[0]
    left, right = [], []
    left_med, right_med = 0, 0

    for i in nums:
        if i < med:
            left_med += 1
        elif i > med:
            right_med += 1
        if i in numbers:
            if i < med:
                left.append(i)
            elif i > med:
                right.append(i)
    if left_med > right_med:
        return median(left)
    elif left_med < right_med:
        return median(right)
    return med


# создаем уникальный список
m = 2
nums = []
for _ in range(2*m+1):
    j = randint(0, 99)
    if j not in nums:
        nums.append(j)


print(nums)
print(median(nums))
