# Пример кода для вычисления ежемесячного платежа по кредиту

user_name = input("Ведите имя: ")
credit = input("Размер кредита: ")
duration = input("Срок кредита: ")
percent = input("Процентная ставка: ")

credit = float(credit)
duration = int(duration)
percent = float(percent)

pay = (credit / duration) + ((credit * percent) / 12)
print(pay)
