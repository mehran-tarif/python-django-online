# first_name = "Mehran"
# last_name = "Tarif"
# age = 23.5

# age += 2

# mystr = "Hello {} {}, your age is: {} years old.".format(first_name, last_name, age)

# print(mystr)

# name = "Mehran"
# age = 23
# myfloat = 10.5

# print(type(name))
# print(type(age))
# print(type(myfloat))

# name = "Hello world, i love world and i live in world."

# print(name[-10:-1])

# int("2")
# str(2.5) = "2.5"
# float(2) = 2.0
# 
# number = 2.1
# mystr = "10"
# print(number)

# number = 17

# print(int(number ** 0.5))

# mybool = True
# mybool = False
# age = 23 # int
# myfloat = 23.0 #float

# and
# or
# number = 55

# if number % 2 == 0:
# 	print("Yes! 2")
# elif number % 5 == 0:
# 	print("Yes! 5")
# elif number % 7 == 0:
# 	print("Yes! 5")
# elif number % 9 == 0:
# 	print("Yes! 5")
# elif number % 11 == 0:
# 	print("Yes! 5")
# else:
# 	print("No!")

# list
# tuple
# set
# dict

# students = ["Mehran", "Ali", "Sara"]

# for student in students:
# 	print("Hello student: {}".format(student))


# students = list(enumerate(students))

# print(students)

# for i, student in students:
# 	print("{}: {}".format(i + 1, student))

# students = ["Mehran", "Ali", "Sara"]

# students.pop(1)

# print(students)
# students = ["Mehran", "Ali", "Sara"]
# students = ("Mehran", "Ali", "Sara")

# students = list(students)
# students[0] = "hossein"
# students = tuple(students)

# for student in students:
# 	print("Student: {}".format(student))

# my_list = [9,7,52,1,4,12,3,11,1,1,1,1]
# my_list = set(my_list)
# my_list = list(my_list)
# my_list.reverse()
# my_list.sort()

# my_set = {"apple", "banana"}

# my_set.update(["dog", "cat"])

# print(my_set)

# my_dict = {
# 	"name": "Mehran",
# 	'age': 23,
# 	'con': "Iran",
# }

# print(list(my_dict.values()))
# print(list(my_dict.keys()))
# print(list(my_dict.items()))
# for key, value in my_dict.items():
# 	print("{} is {},".format(key, value))
# my_dict = {
# 	"name": "Mehran",
# 	'age': 23,
# 	'con': "Iran",
# }

# print(my_dict.get("last"))
# students = ["Mehran", "Ali", "Sara"]

# try:
# 	print(students[2])
# except Exception as e:
# 	print("This number not found.")
# else:
# 	print("Ok, number found.")
# finally:
# 	print("operation done!")
# try:
# 	if students[56]:
# 		print(students[56])
# except:
# 	print("This number not found.")

# for i in range(20):
# 	if i == 11:
# 		continue
		# break
# 	print(i)

# def add(x, y):
# 	return x+y

# sum_number = add(6, 7) + 20
# print(sum_number)

def is_prime():
	number = input("Please enter a number: ")
	try:
		number = int(number)
	except Exception as e:
		print("Please enter a integer number")
		exit()

	if not type(number) == int:
		print("Please enter a integer number")
		exit()

	if number < 2:
		return False

	prime = True

	for i in range(2, int(number ** 0.5) + 1):
		if number % i == 0:
			prime = False
			break

	return prime

print(is_prime())