#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
num_list = [23, 378, 34, 43, 25, 235]
s_list = num_list.copy()
s_list.sort()

min_num = s_list[0]  # мин
max_num = s_list[-1]  # макс

i_min_num = num_list.index(min_num)  # индекс мин в исходном списке
i_max_num = num_list.index(max_num)  # индекс макс в исходном списке

num_list[i_min_num] = max_num
num_list[i_max_num] = min_num

print(num_list)
