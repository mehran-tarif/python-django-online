class Person():
	# first_name = "Mehran"
	# last_name = "Tarif"
	# age = 23
	# country = "Iran"
	# sex = "male"
	def __init__(self, first_name, last_name, age, country, sex):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country
		self.sex = sex

	def fullname(self):
		return "{} {}".format(self.first_name, self.last_name)

	def say_hello(self):
		print("Hello", self.first_name)


# mehran = Person("Mehran", "Tarif", 23, "Iran", "male")
# sara = Person("Sara", "Moradi", 15, "Iran", "female")

# print(mehran.fullname())
# mehran.say_hello()
# sara.say_hello()

class Student(Person):
	def __init__(self, first_name, last_name, age, country, sex, course):
		super().__init__(first_name, last_name, age, country, sex)
		self.course = course

ali = Student("Ali", "Ahmadi", 25, 'US', 'male', 'python')
# ali.set_course("Python")

print(ali.course)