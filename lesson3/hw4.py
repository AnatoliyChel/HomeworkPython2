#  Определить, какое число в массиве встречается чаще всего.
num_list = [23, 378, 34, 43, 25, 235, 378, 25, 25, 25, 43, 43, 43, 43, 43, 43]
nums = []
count = []

for el in num_list:
    if el not in nums:
        #  добавляем число если первое вхождение
        nums.append(el)
        count.append(1)
    else:
        # увеличиваем счетчик если не первое вхождение
        count[nums.index(el)] += 1

#  объединяем в один список для последующей сортировки
result = []
for i, j in zip(nums, count):
    result.append([i, j])

result_final = sorted(result, key = lambda count: count[1])  # сортируем по второму элементу
print("чаще всего встречается число - ", result_final[-1][0])


