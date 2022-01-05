# import logging

# logging.basicConfig(filename='calc.log', level=logging.INFO)

# def logger(func):
# 	def log_func(*args):
# 		logging.info(f"running '{func.__name__}' with arguments: {args}")
# 		print(func(*args))
# 	return log_func

# @logger
# def add(a,b):
# 	return a + b
# @logger
# def sub(a,b):
# 	return a - b

# sub(6,5)
# # print(add(5,3))


# # def demo(*args):
# # 	print(args)

# # demo(2,2,3,44,5)