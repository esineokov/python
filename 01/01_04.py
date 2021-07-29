# Пользовательский ввод и приведение типов данных
from decimal import Decimal

user_input = input('Введите число: ')

# Приведение к int
print(int(user_input) + 1)

# Приведение к строке
print(str(999) + " text")

# Приведение к float
print(float('33.3') + int('100'))
print(float(1))

# Более точные математически вычисления дробных чисел
a = Decimal('3.14')
b = 1
c = a + b
print(c)
