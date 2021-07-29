# Другие примеры
from decimal import Decimal

# Преобразование списка в кортеж и обратно
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
print(list(my_tuple))

# Вложенность списка может быть произвольная
test = [(1, 2, 3), [4, 5, 6], Decimal('123')]
print(test)

# Сортированный список с уникальными значениями (множество)
my_set = set([1, 2, 3, 3, 3, 0])
print(my_set)

# Неизменяемый сортированный список с уникальными значениями (множество)
my_frozenset = frozenset([1, 2, 3])
print(my_frozenset)

