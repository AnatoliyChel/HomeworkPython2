#  Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import numpy as np
num = input("Введите трехзначное число")
if len(num) != 3:
    print("Число не трехзначное")
else:
    spisok = [int(el) for el in list(num)] # преобразуем в список int из str
    print(f"Сумма {sum(spisok)}")
    print(f"Произведение {np.prod(np.array(spisok))}")