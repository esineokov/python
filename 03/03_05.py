# Словари

# Пример словаря
my_dict = {'name': 'Петя', 'age': 20}

# Пример списка словарей
my_list_dicts = [
    {'name': 'Петя', 'age': 20}, {'test': 'Вася', 'av': 30}, {'ol': 'Ира', 'pop': 21}
]

# Перебираем список словарей с обращением к конкретному ключу
for user in my_list_dicts:
    if user['age'] >= 21:
        print(user['name'])

# Перебрать список ключей в словаре
for key in my_dict.keys():
    print(key)

# Перебрать список значений в словаре
for key in my_dict.values():
    print(key)

# Перебор словарей вложенных в список
for d in my_list_dicts:
    for k, v in d.items():
        print(k, ' - ', v)

# Перебор словарей вложенных в список без дополнительной конструкции for
for name, age in my_list_dicts:
    print(name, age)


# Еще один список объявить словарь
my_new_dict = dict(a='text', b='строка')
print(my_new_dict)

# Приведение генератора к словарю
my_list = list(range(0, 10))
print(my_list)

# Минимальное и максимальное значение в словаре
print(min([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))

# Срез создает копию списка, но не данных. Это видно в примере, где вложенный список меняется в обоих переменных
a = [1, 2, 3, [4, 5, 6]]
b = a[-1:]
a[3].append(9)
print(a, b)

# Проверка наличия значения в списке
a = [1, 2, 3]
if 1 not in a:
    print("ее нет")
else:
    print("есть")

# my_dict = {'a': 1, 'b': 2}
