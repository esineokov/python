my_dict = dict().fromkeys(['name', 'surname'])
print(my_dict)
# -----

my_dict2 = dict().fromkeys(['name', 'surname'], 'unknown')
print(my_dict2)

# ----

my_dict3 = dict(a=10)
print(my_dict3.setdefault('a', 2))
print(my_dict3)


# --------
my_dict4 = dict()
print(my_dict4.get('a', 999))
# -----

users = {
    'petya': {
        'name': 'petya', 'surname': 'ivanov', 'age': 22, 'pets': {
            'cat': {
                'name': 'murzik', 'age': 1
            },
            'dog': {
                'name': 'bobik', 'age': 2
            }
        }
    }
}

print(users['petya']['pets']['cat'])
# ---------------


users = {
    'petya': {
        'name': 'petya', 'surname': 'ivanov', 'age': 22, 'pets': [
            {
                'age': 1, 'type': 'cat'
            },
            {
                'name': 'bobik', 'age': 2, 'type': 'dog'
            }
        ]
    }
}

print(users['petya']['pets'][1]['name'])

# -------
print("-------")
for pet in users['petya']['pets']:
    print(pet.get('name', 'unknown'))
