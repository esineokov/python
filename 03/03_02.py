# Методы работы со строками

txt = "Строка"
ztxt = "Строка"

# lower - в нижний регистр
# upper - в верхний регистр
print(txt.lower())
print(txt.upper())
print(txt.upper() == ztxt.upper())

# Привидение строки к list
# Раскладывает посимвольно
a = "Привет!"
print(list(a))

# Строке можно перебрать также как и список
for i in a:
    print(i)

# split - разбиение строки на список
b = "привет! Как дела?"
# ! - разделитель, по которому делится строка
c = b.split("!")

# join - объединение элементов списка в строку с указанием разделителя
print(c)
print("!".join(c))

# Другие методы строк
print(b.capitalize())
print(b.index("!"))
print(b.startswith("K"))
print(b.endswith("?"))

# Форматирование строк. f-строки
z = "Привет {name}! Как дела? {age}".format(name="Женя", age=10, text=1)
name = "Петя"
age = 22
z1 = f"Привет {name}! Как дела? {age}"
print(z1)


# Пример задачки: сумма цифр в строке
my_str = input("Введи число: ")
summa = 0
for i in my_str:
    summa += int(i)

print(summa)

# Замена подстроки в строке

txt = "Привет! Как дела ."
new_txt = txt.replace(" .", ".")
print(new_txt)
