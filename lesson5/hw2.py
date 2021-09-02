"""Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

dict_hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
                "d": 13, "e": 14, "f": 15}
dict_rev = {value: key for key, value in dict_hex.items()}

def hex_to_dec(hex_num):
    decim = 0
    temp_el = 0
    hex_num.reverse()
    for el_index, el in enumerate(hex_num):
        temp_el = dict_hex.get(el.lower())
        decim += temp_el*(16**el_index)
    return decim

def dec_to_hex(dec_num):
    temp = 1
    hex_num = deque()
    while (temp > 0):
        temp = dec_num // 16
        dec_num -= temp * 16
        hex_num.append(dict_rev.get(dec_num))
        dec_num = temp
    hex_num.reverse()
    return hex_num

hex_num1 = list(input("Введите число 1 "))
hex_num2 = list(input("Введите число 2 "))

hex_num11 = hex_to_dec(hex_num1)
hex_num21 = hex_to_dec(hex_num2)
summa = hex_num11 + hex_num21
multiple = hex_num11 * hex_num21
print(dec_to_hex(summa))
print(dec_to_hex(multiple))



