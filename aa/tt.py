class A():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	@property
	def a(self):
		...

	@a.setter
	def a(self, x, y):
		self.x = x
		self.y = y


z = A(2, 3)
# z.a = None,4, 5