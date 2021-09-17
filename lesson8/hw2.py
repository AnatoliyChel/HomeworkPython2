"""Закодировать любую строку по алгоритму Хаффмана."""


class Node:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


# Возвращает крайнюю правую букву в листе дерева и путь до нее
def search(node, path='',):
    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        spam = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam
    if node.left is not None and node.left.value != 0:
        spam = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam


user_string = input('Введите строку для кодирования:\n')

# Собираем словарь буква - частота повторения
letter_dict = {}
for i in user_string:
    if i not in letter_dict:
        letter_dict[i] = 1
    else:
        letter_dict[i] += 1

# Создаем элементы дерева из букв на основе словаря
node_list = list([Node(letter_dict[i], i) for i in letter_dict])

# Пересоздаем структуру дерева с соседями
for i in range(len(letter_dict)-1):
    node_list.sort(key=lambda node: node.value)
    first_el = node_list.pop(0)
    second_el = node_list.pop(0)
    new_node = Node(first_el.value + second_el.value, left=first_el, right=second_el)
    node_list.insert(0, new_node)
node_tree = node_list[0]  # верхний элемент дерева

# Таблица перевода
tr_table = {}
for _ in range(len(letter_dict)):
    k = search(node_tree)
    tr_table[k[0]] = k[1]

print(f'Оригинальная строка: {user_string}')
print('Кодированная строка:')
for el in user_string:
    print(tr_table[el], end=' ')

