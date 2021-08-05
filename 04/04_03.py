# while [1, 2, 3]:
#     print('text')
#
# while True:
#     print('text')


# a = [0]
# print(bool(a))
#
# if bool([1,2,3]):
#     print('text')

my_list = [1, 2, 3]
while my_list:
    print(my_list.pop())
# -----

my_list = ['a', 'b', 'c', 'a', 'a']
while 'a' in my_list:
    my_list.remove('a')