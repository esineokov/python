import sys

my_tuple = (1, 2, 3)
print(type(my_tuple))

my_tuple = tuple([1, 2, 3])
print(my_tuple)

my_str = list("Я длинная строка")
my_tuple = tuple(my_str)

print(sys.getsizeof(my_str))
print(sys.getsizeof(my_tuple))
# ------

my_tuple_one = (1,)
print(type(my_tuple_one))

#---------

my_tuple_one2 = 1,
print(type(my_tuple_one2))

for i in my_tuple:
    print(i)

# ----

a = "text_a"
b = "text_b"
a, b = b, a
print('a', '=', a)
print('b', '=', b)


a, b = [1, 2]
# -------

my_tuple = (1, 2, 3, [4, 5, 6])
print(my_tuple)
my_tuple[3].append(999)
print(my_tuple)
# my_tuple[0] = 100

# -----
while (1,):
    print('tuple')
    break