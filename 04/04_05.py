my_set = set()

my_set = set([1,2,3,4,5,5,5,])
print(my_set)

my_set.add('10')
print(my_set)

my_list = [1,2,3,4,5]
my_set = set()

for i in my_list:
    my_set.add(i)


#--------
my_set = {1, 2, 3, 4}
print(type(my_set))


# print(my_set[0])
# ------

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

c = a | b
print(c)

d = a & b
print(d)

e = a - b
print(e)
#-----

my_dict = {'key': 'value'}
my_dict2 = dict()
my_dict2['key'] = 'value'
print(type(my_dict))
print(type(my_dict2))
