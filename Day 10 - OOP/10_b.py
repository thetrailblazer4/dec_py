
class Emp:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last= last
		self.pay = pay
		self.email = first + '.'+last +'@company.com'


	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(float(self.pay) * self.raise_amt)

class Dev(Emp):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

		



emp_1 = Dev('John', 'K', 50000, 'Python')
emp_2 = Emp('Jane', 'M', '60000')

print(emp_1.prog_lang)
print(emp_1.raise_amt)


print(emp_2.prog_lang)
print(emp_2.raise_amt)

