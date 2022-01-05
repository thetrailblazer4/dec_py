# LEGB --> Local --> Enclosing --> Global --> Builtins

# x = 'global x'

# def demo(z):
# 	# x = 'local y'
# 	print(z)

# demo('Hi')
# # print(z)



# def max():
# 	pass

# nums = [1,2,6,4,3,5]
# print(maxs(nums))

# import builtins

# print(dir(builtins))
# print(help(min))


x = 'global x'

def outer():
	x = 'outer x'

	def inner(): 
		x = 'inner x'
		print(x)
	inner()
	print(x)

outer()
print(x)
	

