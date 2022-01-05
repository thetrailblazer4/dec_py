
# class Emp:

# 	raise_amt = 1.04

# 	def __init__(self, first, last, pay):
# 		self.first = first
# 		self.last= last
# 		self.pay = pay
# 		self.email = first + '.'+last +'@company.com'


# 	def fullname(self):
# 		return f"{self.first} {self.last}"

# 	def apply_raise(self):
# 		self.pay = int(float(self.pay) * self.raise_amt)

# class Dev(Emp):
# 	raise_amt = 1.10

# 	def __init__(self, first, last, pay, prog_lang):
# 		super().__init__(first, last, pay)
# 		self.prog_lang = prog_lang

		
# class Manager(Emp):
# 	def __init__(self, first, last, pay, employees=None):
# 		super().__init__(first, last, pay)

# 		if employees is None:
# 			self.employees = [] 
# 		else:
# 			self.employees = employees

# 	def add_emp(self, emp):
# 		if emp not in self.employees:
# 			self.employees.append(emp)

# 	def remove_emp(self, emp):
# 		if emp in self.employees:
# 			self.employees.remove(emp)

# 	def print_emps(self):
# 		for emp in self.employees:
# 			print(emp.fullname())


# emp_1 = Dev('John', 'K', 50000, 'Python')
# emp_2 = Emp('Jane', 'M', '60000')
# mgr = Manager('Kate', 'M', 90000)

# mgr.add_emp(emp_1)
# mgr.add_emp(emp_2)
# mgr.remove_emp(emp_1)
# mgr.print_emps()
