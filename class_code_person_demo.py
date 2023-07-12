class Person:
    # constructor
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    # internal function
    def myfunc(self):
        print("Hello! My name is " + self.name + ".")
    def introduce_age(self):
        print("I'm " + str(self.age) + " years old.")
    def introduce_country(self):
        print("I'm from " + self.country + ".")
p1 = Person("John", 36, "America")
p1.myfunc()
p1.introduce_age()
p1.introduce_country()
p2 = Person("Alice", 18, "America")
p2.myfunc()
p2.introduce_age()
p2.introduce_country()