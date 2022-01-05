# # f = open('cal.log')

# # print(f.read())

# # f.close()

# # print(f.closed)

# # try:
# # 	pass
# # except:
# # 	pass
# # else:
# # 	pass
# # finally:
# # 	pass


# '''
# FileNotFoundError
# NameError
# '''
# try:
# 	f = open('cal.log')
# except FileNotFoundError as e:
# 	print(e)

# except NameError as e:
# 	print(e)

# except Exception as e:
# 	print(e)

# else:
# 	print(f.read())
# 	f.close()
# finally:
# 	print('This is executing...')



