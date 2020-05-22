class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

	def primeter(self):
		return (self.length + self.width) * 2

# r = Rectangle(1, 2)
# print(r.primeter())

class Squere(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)

# s = Squere(5)
# print(s.area())

class Cube(Squere):
	def surface_area(self):
		return (super().area()) * 6

	def volume(self):
		return (super().area()) * self.length

c = Cube(2)
print(c.volume())