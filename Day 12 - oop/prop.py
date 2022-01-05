class Emp:

	def __init__(self, first, last, pay):
		self.first = first
		self.last= last
		self.pay = pay
		# self.email = first + '.'+last +'@company.com'

	@property
	def email(self):
		return f"{self.first}.{self.last}@company.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

emp_1 = Emp('John', 'K', 50000)

emp_1.first = 'Kate'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)