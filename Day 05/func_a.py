# # '''DRY -> Don't Repeat yourself!'''

# # def message(greeting, name='You'):
# # 	return f'{name}, {greeting} World!'

# # print(message('Hello', 'John'))


# def emp_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)

# prog_lang = ['Python', 'java']

# info = {'name':'John', 'Age': 30}


# emp_info(*prog_lang, **info)




prog_lang = ['Python', 'java', 'C']


def find_index(to_search, target):
	for i, value in enumerate(to_search):
		if value == target:
			return i
	return -1

print(find_index(prog_lang, 'Python'))
