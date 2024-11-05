from people import Faculty
from people import Student

def main():
    faculties = []
    student_list = []
    faculty_name = []
    student_name = []

    while True:
        # Print the main menu
        print("*** TUFFY TITAN STUDENT/FACULTY MAIN MENU")  
        print("1. Add faculty")
        print("2. Print faculty")
        print("3. Add student")
        print("4. Print student")
        print("9. Exit the program")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        
        # Add faculty
        if choice == 1:
            # Faculty.add_faculty(self=None, faculties=None)
            # def add_faculty(self, fname, lname, dpt):
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            department = input("Enter department: ")
            faculties.append(Faculty(fname=firstname,  lname=lastname, dpt=department))
            # faculties.append(firstname, lastname, department)
            full_name = f"{firstname} {lastname}"
            faculty_name.append(full_name)
            
        elif choice == 2:
            # Faculty.print_faculty(self=None, faculties=None)
            print("======================= FACLUTY =======================")
            print("Record  Name                  Department")
            print("======  ====================  ==========================")
            for i, Faculty in (faculties):
                print(f"{i:<6}       {Faculty.fname:<19} {Faculty.lastname:<35}           {Faculty.department}")
        
        # Add student
        elif choice == 3:
            # Student.add_student(student_list)
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            classyear = input("Enter classyear: ")
            major = input("Enter major: ")
            advisor = input("Enter advisor: ")
            student_list.append(Student(firstname, lastname, classyear, major, advisor))
        
        # Print student
        elif choice == 4:
            Student.print_student(student_list)
            print("======================= STUDENT =======================")
            print("Record  Name                  Department")
            print("======  ====================  ==========================")
            # for i, student in enumerate(student_list):
            print(f"{i}       {Student.firstname} {Student.lastname}           {Student.department}")
        
        # Exit the program
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

