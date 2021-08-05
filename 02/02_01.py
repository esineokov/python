# Список
#        0        1         2          3
cars = ['opel', 'mazda', 'mercedes', 'audi']
print(cars)

# Обращение по индексу
print(cars[0])

# Добавление в список
cars.append('Jeep')
cars.append('uaz')
cars.append('Jeep')
print(cars)

# Удаление из списка по индексу
del cars[0]
print(cars)

# Удаление из списка по значению
cars.remove('Jeep')
print(cars)

# Удаление из списка по значению (2)
numb = [1, 2, 3]
print(numb)
numb.remove(3)
print(numb)

# Добавление в список с указанием индекса встаски
cars.insert(2, 'TEST')
print(cars)

# Удаление из списка с возвратом удаляемого значения
a = cars.pop(0)
print(a)
print(cars)

# Сортировка списка
cars.sort()
print(cars)

# Сортировка списка (2)
b = sorted(cars)
print(b)

# Цикл для итерации по списку
for _ in cars:
    print(_)

# Цикл по генератору
for i in range(2):
    print("текст")
    if i == 0:
        break
    input("введите данные")

# Генератор для python 2
# xrange()


