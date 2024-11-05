class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Faculty(Person):
    def __init__(self, fname, lname, dpt):
        Person.__init__(self, fname, lname)
        # self.department = department
        self.department = dpt

# class Student:
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
    
#     def set_class(self, classyear):
#         self.classyear = classyear
    
#     def set_major(self, major):
#         self.major = major
    
#     def set_advisor(self, Faculty):
#         self.advisor = Faculty

class Student(Person):
    def __init__(self, fname, lname):
        # Directly call the initializer of Person
        Person.__init__(self, fname, lname)  
    
    def set_class(self, classyear):
        self.classyear = classyear
    
    def set_major(self, major):
        self.major = major
    
    def set_advisor(self, Faculty):
        self.advisor = Faculty
