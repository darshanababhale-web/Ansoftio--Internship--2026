# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class (Inheritance)
class Student(Person):
    def __init__(self, name, age, course):
        # Calling parent constructor
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print("Course:", self.course)


# Object creation
s1 = Student("Darshana", 22, "MCA")

# Display details
s1.display_student()
