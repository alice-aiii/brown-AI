class Course:
    def __init__(self, class_name, difficulty, teacher, max):
        self.class_name = class_name
        self.difficulty = difficulty
        self.teacher = teacher
        self.max = max
    def introduce(self):
        return(self.teacher + " will teach " + self.class_name + ". This class has a difficulty of " + str(self.difficulty) + " and the max number of students enrolled can be " + str(self.max) + ".")
# c1 = Course("AI", 3, "Benedict", 25)
# c1.introduce()

class Student:
    def __init__(self, name, age, grade, course):
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course
    def introduce(self):
        print(self.name + " is " + str(self.age) + " years old and is in grade " + str(self.grade) + ".")
    def enroll(self):
        print(self.name + " has enrolled in this class.")
    def drop_out(self):
        print(self.name + " has dropped out of this class.")
    def introduce_course(self):
        # print(self.course.introduce())
        print(self.name, ": ", self.course.introduce())

# s1 = Student("Alice", 18, 12, c1)
# s1.introduce()
# s1.enroll()
# s1.drop_out()
# s1.introduce_course()

