# Пример использования генератора
names = []
for _ in range(3):
    name = input("Введите имя: ")
    names.append(name)

print(names)

# Пример цикла while
i = 0
while i < 10:
    print(i)
    i += 1
    # i = i + 1

# Пример цикла while (2)
i = 0
while True:
    print('abc')

    i += 1

    if i > 10:
        break

