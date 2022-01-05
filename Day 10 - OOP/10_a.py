# '''
# Object-oriented programming (OOP) is a programming 
# paradigm based on the concept of 
# "objects", which can contain data and code: 
# data in the form of fields (often known as attributes or properties), and 
# code, in the form of procedures (often known as methods).

# Class and Instances/objects

# '''


# class Emp:

# 	raise_amt = 1.04
# 	num_of_emps = 0

# 	def __init__(self, first, last, pay):
# 		self.first = first
# 		self.last= last
# 		self.pay = pay
# 		self.email = first + '.'+last +'@company.com'

# 		Emp.num_of_emps += 1

# 	def fullname(self):
# 		return f"{self.first} {self.last}"

# 	def apply_raise(self):
# 		self.pay = int(float(self.pay) * self.raise_amt)

# 	@classmethod
# 	def set_raise_amt(cls, amount):
# 		cls.raise_amt = amount

# 	@classmethod
# 	def from_str(cls, emp_str):
# 		first, last, pay = emp_1_str.split('-')
# 		return cls(first, last, pay)

# 	@staticmethod
# 	def is_workday(day):
# 		if day.weekday() == 5 or day.weekday() == 6:
# 			return False

# 		return True


# 	def __repr__(self):
# 		return f"Emp('{self.first}', '{self.last}', {self.pay})"

# 	def __str__(self):
# 		return f"{self.fullname()} - {self.email}"



# emp_1 = Emp('John', 'K', 50000)
# emp_2 = Emp('Jane', 'M', '60000')

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# # emp_1_str = 'John-K-50000'

# # new_emp_1 = Emp.from_str(emp_1_str)

# # # first, last, pay = emp_1_str.split('-')
# # # new_emp_1 = Emp(first, last, pay)

# # # Emp.set_raise_amt(1.08)
# # # print(emp_1.raise_amt)
# # # print(new_emp_1.first)


# # import datetime

# # my_date = datetime.date(2021,12,26)

# # print(Emp.is_workday(my_date))

# # # print(datetime.__file__)