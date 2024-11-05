class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Faculty:
    def __init__(self, fname, lname, dpt):
        Person.__init__(self, fname, lname)
        # self.department = department
        self.department = dpt

    # def add_faculty(self, faculty_list):
    #     firstname = input("Enter first name: ")
    #     lastname = input("Enter last name: ")
    #     department = input("Enter department: ")
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.department = department
    #     faculty_list.append(self)

class Student:
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
    
    def set_class(self, cy):
        self.classyear = cy
    
    def set_major(self, major):
        self.major = major
    
    def set_advisor(self, Faculty):
        self.advisor = Faculty

