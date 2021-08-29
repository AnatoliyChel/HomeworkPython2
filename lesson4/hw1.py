#  Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#  Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import timeit
from random import randint
num_list = [randint(0, 10000000) for _ in range(1, 10000000)]
start_time = timeit.timeit()

s_list = num_list.copy()
s_list.sort()

min_num = s_list[0]  # мин
max_num = s_list[-1]  # макс

i_min_num = num_list.index(min_num)  # индекс мин в исходном списке
i_max_num = num_list.index(max_num)  # индекс макс в исходном списке

num_list[i_min_num] = max_num
num_list[i_max_num] = min_num


# вариант 2
# min = 0
# min_index = 0
# max = 0
# max_index = 0
# for i in range(0, len(num_list)-1):
#     if num_list[i] > num_list[i + 1] and num_list[i] > max:
#         max = num_list[i]
#         max_index = i
#         min = num_list[i + 1]
#         min_index = i+1
#     elif num_list[i] < num_list[i + 1] and num_list[i + 1] > max:
#         max = num_list[i + 1]
#         max_index = i + 1
#         min = num_list[i]
#         min_index = i
# num_list[min_index] = max
# num_list[max_index] = min


# print(num_list)
# print(min_index, max_index)
end_time = timeit.timeit()

print(end_time-start_time)

# вариант 1 t = 0,0045
# вариант 2 t = 0,0045
# оба варианта показали похожую скорость работы, следовательно функция сортировки сравнима по скорости с перебором в цикле
# но имеет более короткую запись

