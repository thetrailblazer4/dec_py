'''
In computer science, 
a data structure is a data organization, management, and storage format 
that enables efficient access and modification
'''

# greeting = 'Hello, Hi, Hey'
# greeting = ['Hello', 'Hi' , 'Hey']

# print(greeting.index('Hey'))
# list_2 = ['Bye', 'Hola']

# greeting.append('Hola')
# greeting.insert(1, 'Hola')
# greeting.extend(list_2)

# greeting.remove('Hey')
# removed = greeting.pop(1)
# print(removed)

# nums = [2,1,5,3,4]

# nums.sort(reverse=True)
# print(nums)

# sorted_nums = sorted(nums)

# print(sorted_nums)



# print(greeting)

# print('Hi' in greeting)

# for i in greeting:
# 	print(i)

# Access a list

# for h in greeting:
# 	print(h)

# for index, item in enumerate(greeting):
# 	print(index, item)

# print(greeting)

# print(greeting[2])
# print(greeting[7:])


# from list to str
greeting = ['Hello', 'Hi' , 'Hey']

new_str = ' - '.join(greeting)
print(type(new_str))

# print(new_str)

# from str to lst

new_list = new_str.split(' - ')
print(type(new_list))