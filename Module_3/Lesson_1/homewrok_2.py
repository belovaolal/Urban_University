'''
Практическое задание по работе в Pycharm - "Переменные".

Цель: научиться правильно называть переменные и взаимодействовать с ними.

Задача:
Напишите 4 переменных которые буду обозначать следующие данные:
Количество выполненных ДЗ (запишите значение 12)
Количество затраченных часов (запишите значение 1.5)
Название курса (запишите значение 'Python')
Время на одно задание (вычислить используя 1 и 2 переменные)
Выведите на экран(в консоль), используя переменные, следующую строку:
Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

Пример написанного кода:
first_name = 'Vasya'
apple_count = 10
second_name = 'Petya'
orange_count = 15
print(first_name, 'дал', second_name, apple_count, 'яблок и', orange_count, 'апельсинов')

Результат выполнения кода:
Vasya дал Petya 10 яблок и 15 апельсинов

Примечания:
Для вывода значений на экран используйте функцию print(a, b, c), где a, b, c - данные которые выводятся на экран.
Для названия переменных используйте только: латинские буквы, не начинайте запись с числа, пишите в змеином регистре(разделяя слова символом '_')
Пробелы между словами и символами ':' ',' можно ставить на своё усмотрение.
'''

# Переменные для хранения данных
homework_count = 12
hours_spent = 1.5
course_name = 'Python'
time_per_task = hours_spent / homework_count

# Вывод информации на экран
print(f"Курс: {course_name},"
      f"всего задач: {homework_count},"
      f"затрачено часов: {hours_spent:.1f},"
      f"среднее время выполнения {time_per_task:.3f} часа.")

'''
Объяснение кода:
Переменные:
1. `homework_count` хранит количество выполненных домашних заданий.
2. `hours_spent` хранит количество затраченных часов.
3. `course_name` хранит название курса.
4. `time_per_task` вычисляет среднее время на выполнение одного задания.

Вывод:
Используется функция `print()` для вывода информации.
Внутри функции `print()` используется f-строка для форматирования вывода.
Это позволяет вставлять значения переменных непосредственно в строку текста, используя фигурные скобки `{}`.
`.1f` и `.3f` после переменных в f-строке указывают количество знаков после запятой для чисел с плавающей точкой (1 знак после запятой для `hours_spent` и 3 знака для `time_per_task`).
'''