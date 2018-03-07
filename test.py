
cars = ["bmw", "audi", "toyota", "ford"]

print("cars list:")
print(cars)

cars.sort()
print("sorted cars list:")
print(cars)

cars.sort(reverse=True)
print("sorted in reverse cars list:")
print(cars)

#function returning second character as key to sort or compare
def key(string):
	return string[1]
	
cars.sort(key=key)
print("sorted by second character cars list:")
print(cars)

#cmp is not sort keyword anymore in python 3
#function comparing by last character in string
def compare(string1, string2):
	c1 = string1[len(string1) - 1]
	c2 = string2[len(string2) - 1]
	if(c1 < c2):
		return -1
	if(c2 > c1):
		return 1
	return 0
	
print()
#####################################
class Person:
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last
		
	def Name(self):
		return self.firstname + " " + self.lastname
		
class Employee(Person):
	def __init__(self, first, last, staffnum):
		Person.__init__(self, first, last)
		self.staffnumber = staffnum
		
	def GetEmployee(self):
		return self.Name() + ", " + self.staffnumber
		
x = Person("Merge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

print()
from python_hello import IPaddressMask

addr = IPaddressMask("192.168.10.10/25")
print(addr)

print()
########################################3
print("example of exception")
try:
	fh = open("testfile", "r")
	fh.write("This is my test file for exception handling!")
except IOError:
	print("Error")
else:
	print("Success")
finally:
	print("finally block")
	

	


	
