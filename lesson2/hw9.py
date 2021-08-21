"""Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
nums = input("введите числа через пробел ").split(" ")
sums = []
# print(nums)
for num in nums:
    sums.append(sum([int(sub_num) for sub_num in list(num)]))

sums_end = sorted(sums)
print("наибольшее число и сумма цифр ", nums[sums.index(sums_end[-1])], sums_end[-1])