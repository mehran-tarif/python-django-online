def add(x , y):
	return x + y

def zarb(x, y):
	return x * y

class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

	def primeter(self):
		return (self.length + self.width) * 2


class Squere(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)


class Cube(Squere):
	def surface_area(self):
		return (super().area()) * 6

	def volume(self):
		return (super().area()) * self.length