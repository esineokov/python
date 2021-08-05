# Составление список (list comprehension )

# Пример 1
a = ['Петя', 'Катя', 'Ира', 'Женя']
b = [name + " текст" for name in a]
print(b)

# Пример 2
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [i**2 for i in c if i > 5]
z = [[i, j] for i in [1, 2, 3] for j in [5, 6, 7] if i >= 2 and j < 7]
print(z)


# pass - выполнить строку без действия. Нельзя оставить просто пустую строку.
for i in c:
    pass

# ... - аналогично pass
if a == b:
    ...
else:
    c = 1


def test():
    ...

