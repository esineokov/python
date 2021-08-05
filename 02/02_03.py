# Генерация случайных чисел
import random

# Генерация случайного числа с плавабщей точкой от 0 до 1
a = random.random()
print(a)

# Генерация случайного целого числа в указанном диапазоне
b = random.randint(1, 100)
print(b)

# Случайная перестановку элементов массива
numb = [1, 2, 3, 4, 5]
random.shuffle(numb)
print(numb)

# Выбор случайного элемента из списка
names = ['name1', 'name2', 'name3']
c = random.choice(names)
print(c)

