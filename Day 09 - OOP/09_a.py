'''
Object-oriented programming (OOP) is a programming 
paradigm based on the concept of 
"objects", which can contain data and code: 
data in the form of fields (often known as attributes or properties), and 
code, in the form of procedures (often known as methods).

Class and Instances/objects

'''


class Emp:

	raise_amt = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last= last
		self.pay = pay
		self.email = first + '.'+last +'@company.com'

		Emp.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(float(self.pay) * self.raise_amt)

print(Emp.num_of_emps)
emp_1 = Emp('John', 'K', 50000)
emp_2 = Emp('Jane', 'M', '60000')
print(Emp.num_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.raise_amt)
# print(Emp.raise_amt)

# emp_2.raise_amt = 1.05

# print(emp_1.raise_amt)
# print(Emp.raise_amt)