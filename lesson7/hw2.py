"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform

nums = [uniform(0, 49.99999) for _ in range(12)]


def merge_sort(numbers):

    def merge(left, right):
        i = j = 0
        new_num = []
        while i < len(left) or j < len(right):
            if i >= len(left):
                new_num.append(right[j])
                j += 1
            elif j >= len(right):
                new_num.append(left[i])
                i += 1
            elif left[i] < right[j]:
                new_num.append(left[i])
                i += 1
            else:
                new_num.append(right[j])
                j += 1
        return new_num

    length = len(numbers)
    if length > 1:
        left_nums = merge_sort(numbers[:length // 2])
        right_nums = merge_sort(numbers[length // 2:])
        return merge(left_nums, right_nums)
    else:
        return numbers


print(nums)
print(merge_sort(nums))
