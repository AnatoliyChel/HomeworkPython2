# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

nums = [0] * 8  # (24*8)+(40+8*8) = 296 байт

for i in range(2, 100):  # i = 24 байта
    for j in range(2, 10):  # j = 24 байта
        if not i % j:
            nums[j-2] += 1

for el in range(2, 10):  # el = 24 байта
    print(f"кратны {el} - {nums[el-2]}")
# Python 3.8 OS-64bit общое кол-во памяти 296+24+24+24 = 368 байт




#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import timeit
from random import randint
num_list = [randint(0, 1000) for _ in range(1, 1000)]  # (24*1000)+(40+8*1000) = 32040 байт
start_time = timeit.timeit()

s_list = num_list.copy()  # (24*1000)+(40+8*1000) = 32040 байт
s_list.sort()

min_num = s_list[0]  # мин  #  24 байта
max_num = s_list[-1]  # макс #  24 байта

i_min_num = num_list.index(min_num)  # индекс мин в исходном списке  #  24 байта
i_max_num = num_list.index(max_num)  # индекс макс в исходном списке  #  24 байта

num_list[i_min_num] = max_num
num_list[i_max_num] = min_num
# Python 3.8 OS-64bit общое кол-во памяти 32040+32040+24+24+24+24 = 64176 байт = 62,67 кбайт