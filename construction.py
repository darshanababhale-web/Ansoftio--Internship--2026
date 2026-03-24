class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Taking input from user
name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

# Creating object
s1 = Student(name, age, course)

# Calling function
s1.display()
