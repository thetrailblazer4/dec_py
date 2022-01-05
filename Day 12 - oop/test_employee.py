import unittest
from employee import Emp

class TestEmp(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		print('SetUp')
		self.emp_1 = Emp('John', 'K', 50000)
		self.emp_2 = Emp('Jane', 'M', 60000)

	def tearDown(self):
		print('tearDown')
	
	def test_email(self):
	
		self.assertEqual(self.emp_1.email, 'John.K@company.com')
		self.assertEqual(self.emp_2.email, 'Jane.M@company.com')

		self.emp_1.first = 'Kate'
		self.emp_2.first = 'Tom'

		self.assertEqual(self.emp_1.email, 'Kate.K@company.com')
		self.assertEqual(self.emp_2.email, 'Tom.M@company.com')

	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John K')
		self.assertEqual(self.emp_2.fullname, 'Jane M')

		self.emp_1.first = 'Kate'
		self.emp_2.first = 'Tom'

		self.assertEqual(self.emp_1.fullname, 'Kate K')
		self.assertEqual(self.emp_2.fullname, 'Tom M')


	def test_apply_raise(self):

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 54000)
		self.assertEqual(self.emp_2.pay, 64800)







if __name__ == '__main__':
	unittest.main()