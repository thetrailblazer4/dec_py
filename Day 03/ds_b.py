# Mutable

list_1 = ['Hello', 'Hi' , 'Hey']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Bye'

# print(list_1)
# print(list_2)

# Immutable

# tuple_1 = ('Hello', 'Hi' , 'Hey')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Bye'

# print(tuple_1)
# print(tuple_2)

# messages = {'Hello', 'Hi' , 'Hey', 'Hi', 'Hi','Hey'}

# print('Hi' in messages)
# # print(sets)


# # Empty Lists:
# empty_list = []
# empty_list = list()

# # Empty Tuples:
# empty_Tuple = []
# empty_Tuple = tuple()

# # Empty sets:
# empty_set = {} #<-- not preferred method. It is used for creating dict
# empty_set = set()


# Dict
# {key: value}

emp = {'id':1, 'name':'John', 'prog_lang':['Python','Java']}

for key, value in emp.items():
	print(f'{key} - {value}')

# print(emp.keys())
# print(emp.values())
# print(emp.items())

# emp = {1:1, 'name':'John', 'prog_lang':['Python','Java']}

# emp['phone'] = '333-33333'
# emp['name'] = 'Jane'

# emp.update({'name':'Jane', 'phone':'5555-44444'})

# del emp['id']
# removed = emp.pop('id')
# print(removed)
# print(emp['phone'])
# print(emp)