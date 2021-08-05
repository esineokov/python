def test():
    print('text')


test()
# ------

def expo(a, b=2):
    return a ** b


my_expo = expo(a=2, b=3)
print(my_expo)

# ----
#
# def ret_none():
#     a = 1
#
# var = ret_none()
# print(var)
# # -------
#
# print(expo(a=4, b=5))
# print(expo(b=5, a=10))
#
# # -----
#

def test2(my_list_1, my_list_2):
    """Описываем, что делает функуция sldkfudslkjfsdlkjflsdkjflsdkjfdlskjfsldkjfsdlkfjsdlkjfsldkjfsdlkjfsdlkjfsdlkjfl"""
    my_list_1.append(999)
    my_list_2.append(999)
    return my_list_1, my_list_2

my_new_list_1, my_new_list_2 = test2(my_list_1=[1, 2, 3], my_list_2=[4, 5, 6])
print(my_new_list_1, my_new_list_2)
#
#
# def test3(a):
#     pass
#
# test3(a=tuple())
#
#

