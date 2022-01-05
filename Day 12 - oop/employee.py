class Emp:

	raise_amt = 1.08

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

	def apply_raise(self):
		self.pay = int(float(self.pay) * self.raise_amt)
