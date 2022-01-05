# """
# A programming language is said to have First-class functions 
# when functions in that language are treated like any other variable. 

# For example, 
# in such a language, a function can be passed as an argument to other functions, 
# can be returned by another function and can be assigned as a value to a variable.

# """

# def sqaure(x):
# 	return x * x

# def cube(x):
# 	return x * x * x


# # result = sqaure
# # print(result(2))
# # [1,2,3,4] --> [1,4,9,16]


# def my_func(func, arg_list):
# 	result = []
# 	for i in arg_list:
# 		result.append(func(i))
# 	return result

# print(my_func(sqaure,[1,2,3,4]))
# print(my_func(cube,[1,2,3,4]))



# def outer_func(greeting):
# 	message = greeting

# 	def inner_func():
# 		return message

# 	return inner_func

# new_var = outer_func('Hello')
# new_var_1 = outer_func('Hey')

# print(new_var())
# print(new_var_1())
# print(new_var())
# print(new_var.__name__)


def decorator_func(orig_fun):
	def wrapper_func(*args):
		print('Hello')
		return orig_fun(*args)
	return wrapper_func

@decorator_func
def display():
	print("Display function ran!")

@decorator_func
def sqaure(x):
	print(x * x)

display()

sqaure(5)

# decorated_disp = decorator_func(display)
# decorated_disp()

