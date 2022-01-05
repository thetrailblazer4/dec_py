# f = open('calc.log', 'r')

# print(f.read())

# f.close()

# with open('calc.log', 'r') as f:
# 	for line in f:
# 		print(line, end='')



# with open('calc_new.log', 'a') as f:
# 	f.write('New Line 2')


	# data = f.readline()
	# print(data)


with open('calc.log', 'r') as rf:
	with open('test_calc.log', 'w') as wf:
		for line in rf:
			wf.write(line)