from CourseMM import Course
from CourseMM import Student
from CourseMM import Admin
from CourseDataB import StudentDataB
import random

admin1 = Admin("Edikan", "edi54")
course1 = Course()
course2 = Course()
student1 = Student()
student2 = Student()


student1.createstudent("Edikan", "11900", "Elec")
student2.createstudent("Jakab", "11800", "Mech")


print("are you admin or student?\n type: 1 for admin\n 2. for student ")
ad0 = input("enter selection: ")
while ad0 != "1" or ad0 != "2":
    if ad0 == "1":
        ad1 = input("enter admin name: ")
        ad2 = input("enter admin pass: ")

        if ad1 == admin1.ad_name and ad2 == admin1.ad_pass:
            print("Welcome! Create course to proceed:")

            course1.addcourse(input("enter Instructor: "), input("enter topic: "), input("enter code: "))
            print("Course created!: \n")
            print("instructor: ", course1.instr)
            print("Topic: \n", course1.c_topic)
            print("Course ID: \n", course1.c_id)
            course1.courseFlag = True
            print("______________________________________________________________________________________")
            print("______________________________________________________________________________________")

            print("system functions : \n 1. enroll student\n 2. un-enroll student\n 3. modify course\n "
              "4. delete course\n 5. submit grades")

            ad3 = input("input here: ")

            if ad3 == "1":
                print("enter student Id to enrol: ")
                s_id = input("enter student id: ")
                if s_id == student1.stud_id:
                    course1.enrol(student1.stud_id)
                    print("student enrolled!: ")
                elif s_id == student2.stud_id:
                    course1.enrol(student2.stud_id)
                    print("student enrolled!: ")
                else:
                    print("student not found!")

            elif ad3 == 2:
                course1.enrol(student1.stud_id)
                course1.enrol(student2.stud_id)
                s_id = input("please enter student ID to un-enroll: ")
                if s_id == student1.stud_id:
                    course1.unenrol(student1.stud_id)
                    print("student un-enrolled!: ")
                elif s_id == student2.stud_id:
                    course1.enrol(student2.stud_id)
                    print("student un-enrolled!: ")
                else:
                    print("student not found!")

            elif ad3 == "3":
                co_id = input("enter course id: ")
                if co_id == course1.c_id:
                    course1.modifycourse(course1.c_id)
                    print("instructor: ", course1.instr)
                    print("Topic: \n", course1.c_topic)
                    print("Course ID: \n", course1.c_id)
                else:
                    print("course not found")

            elif ad3 == "4":
                co_id = input("enter course id: ")
                if co_id == course1.c_id:
                    course1.deletecourse(course1.c_id)
                    print("Course deleted!")
                    print("instructor: ", course1.instr)
                    print("Topic: \n", course1.c_topic)
                    print("Course ID: \n", course1.c_id)
                    print("students in course: \n", course1.students)
                    print("student grades: \n", course1.grades)
                else:
                    print("course not found")

# add student1 grade
            elif ad3 == "5":
                course1.enrol(student1.stud_id)
                stud_id = input("enter student id: ")
                if stud_id == student1.stud_id:
                    course1.addstudentgrade(student1.stud_id)
                else:
                    print("student not found")

        else:
            print("You are not authorized to perform action!")

    elif ad0 == "2":
        print("Welcome, select ")
        print("student functions : \n 1. enrol in course\n 2. un-enroll in course\n 3. modify details\n 4. delete your "
          "details")

        course1.addcourse("James", "Software Dev", "ELG5300")

        ad5 = input("enter input: ")

# enrol student in course 1
        if ad5 == "1":
            s_ed = input("enter id: ")
            if s_ed == student1.stud_id:
                course1.enrol(student1.stud_id)
                print("you are enrolled in: ", course1.c_topic)
            else:
                print("re-enter input: ")

        elif ad5 == "2":
            s_ed = input("enter id: ")
            if s_ed == student1.stud_id:
                course1.unenrol(student1.stud_id)
                print("you have dropped: ", course1.c_topic)
            else:
                print("re-enter input: ")

# modify student 1
        elif ad5 == "3":
            s_ed = input("enter id: ")
            if s_ed == student1.stud_id:
                student1.modifystudent(student1.stud_id)
                print("your details have been updated_______")
                print("student name: ", student1.stud_name)
                print("student id: ", student1.stud_id)
                print("student dept: ", student1.stud_dept)
            else:
                print("re-enter input: ")

# delete student 1
        if ad5 == "4":
            stud_id = input("please enter your ID: ")
            if stud_id == student1.stud_id:
                student1.deletestudent(student1.stud_id)
                print("Student deleted!")
            else:
                print("student ID not found")