"""Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib


def substring_count(user_string):
    result_dict = {}
    length = len(user_string) + 1
    for i in range(length):  # первый символ подстроки
        for j in range(i + 1, length):  # длинна подстроки
            if i == 0 and j == length - 1 or user_string[i:j] == " ":  # исключаем полную и пустую строку
                continue
            s = hashlib.sha1(bytes(user_string[i:j].encode("utf-8"))).hexdigest()
            result_dict.update({s: user_string[i:j]})
    return len(result_dict)


user_str = input("input string ")


print(substring_count(user_str))