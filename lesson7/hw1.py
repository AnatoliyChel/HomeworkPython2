""" Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint


def sort_bubble(numbers):
    for j in range(1, len(numbers)):
        count = 0
        for i in range(len(numbers)-j):
            # print(i)
            if numbers[i] > numbers[i+1]:  # если последующий меньше предыдущего
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # меняем местами
                count += 1
        if count == 0:  # если массив уже отсортирован досрочно выходим из функции
            # print(j, i)
            # print("already sorted")
            return numbers
    return numbers


nums = [randint(-100, 99) for _ in range(15)]
# nums = [1,2,3,4,5,6]
print(nums)

print(sort_bubble(nums))
