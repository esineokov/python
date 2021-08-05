# Срезы (slices)

txt = "Привет! Как дела ."

# Выбрать все элементы от 0 до 3 индекс НЕвключительно. То есть, 3й индекс не включается в выборку
z = txt[0:3]
print(z)

# 0й индекс можно не указывать
z1 = txt[:3]
print(z1)

# Последний индекс тоже можно не указывать
z2 = txt[3:]
print(z2)

# Срез с указанием шага
# 2 - шаг. То есть, будет выбран каждый второй элемент
z3 = txt[0:5:2]
print(z3)

# Обратная индексация
#              0        1           2       3
my_list = ['яблоко', 'мандарин', 'банан', 'киви']
#            -4           -3         -2      -1

# Доступ к элементу по обратному индексу
print(my_list[-1])

# Срез с обратными индексами
my_list_new = my_list[-3:-1]
print(my_list_new)

# Быстрый способ инвертировать список
my_list_reverse = my_list[::-1]
print(my_list_reverse)

# Быстрый способ инвертировать строку
my_str = "я строка"
print(my_str[::-1])

# Быстрая копия списка. Копия именно СПИСКА, а не данных!
a = [1, 2, 3]
b = a[:]

a[0] = 100
print(a, b)

# Перебирать список и оожновременно его модифицировать - плохо. Может привести к неожиданным результатам.
# Пример с копией списка:
names_list = ['Петя', 'Вася', 'Костя']
for name in names_list[:]:
    names_list.remove(name)
print(names_list)

# Пример среза с шагом. Может применяться для выбора все нечетных чисел в списке
z = [1, 2, 3, 4, 5, 6, 7, 8]
print(z[::2])
