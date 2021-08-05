# while True:
#     input('Продолжить?')
#     continue
#     print('hello')


#-----
#
# while True:
#     answer = input('Продолжить?')
#     if answer == 'no':
#         break
#     else:
#         continue
#     print('hello')


# -----

number = 0
while number < 15:
    number += 1
    if number % 3 != 0:
        print(number)
# ----
number = 0
while number < 15:
    number += 1
    if number % 3 == 0:
        continue
    else:
        print(number)
