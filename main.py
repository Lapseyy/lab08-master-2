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
            # for faculty in faculties:
            #     print(f"{faculty.firstname:<19} {faculty.lastname:<15} {faculty.department:<25}")
            for i, faculty in enumerate(faculties):
                full_name = f"{faculty.firstname} {faculty.lastname}"
                print(f"{i:<6}  {full_name:<20}  {faculty.department:<25}")
        # Add student
        elif choice == 3:
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            classyear = input("Enter class year: ")
            major = input("Enter major: ")
            advisor_firstname = input("Enter advisor's first name: ")
            advisor_lastname = input("Enter advisor's last name: ")

            # Create the student object with only the required parameters for initialization
            student = Student(fname=firstname, lname=lastname)

            # Use the provided methods to set other attributes
            student.set_class(classyear)
            student.set_major(major)

            # Create a Faculty instance for the advisor and set it
            advisor = Faculty(fname=advisor_firstname, lname=advisor_lastname, dpt="Unknown")  # Specify department if needed
            student.set_advisor(advisor)

            # Append to the list
            student_list.append(student)

        elif choice == 4:
            print("===================================== STUDENTS ======================================")
            print("Name                  Class      Major                      Advisor")
            print("====================  =========  =========================  =========================")
            for student in student_list:
                # Assuming advisor is set as a Faculty object with first and last name attributes
                sfull_name = f"{student.firstname} {student.lastname}"
                advisor_name = f"{student.advisor.firstname} {student.advisor.lastname}" if student.advisor else "No advisor"
                print(f"{sfull_name:<21} {student.classyear:<9} {student.major:<25} {advisor_name}")

        
        # Exit the program
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

