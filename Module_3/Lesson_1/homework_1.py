'''
Практическое задание по уроку "Строки и индексация строк"

Цель: Научиться работать со строками и индексацией строк в Python.
Задача:
Выполните следующие действия в PyCharm:
В переменную example запишите любую строку.
Выведите на экран(в консоль) первый символ этой строки.
Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
Выведите на экран(в консоль) это слово наоборот.
Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')

Вводные данные:
example = 'Топинамбур'

Вывод на экран(в консоль):
Т
р
амбур
рубманипоТ
оиабр
'''

# Задаем строку
example = 'Топинамбур'

# Выводим первый символ строки
print(example[0])

# Выводим последний символ строки (используя отрицательный индекс)
print(example[-1])

# Выводим вторую половину строки (с нечетным количеством символов)
half_length = len(example) // 2 + 1
print(example[half_length:])

# Выводим строку наоборот
print(example[::-1])

# Выводим каждый второй символ строки
print(''.join(example[i] for i in range(0, len(example), 2)))
