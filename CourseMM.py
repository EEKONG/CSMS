import random


class Course:

    def __init__(self):
        self.instr = None
        self.c_topic = None
        self.c_id = None
        self.courseFlag = False
        self.students = None
        self.grades = None

    def addcourse(self, instr, c_topic, c_id):
        self.instr = instr
        self.c_topic = c_topic
        self.c_id = c_id
        self.students = list()
        self.grades = list()

    def enrol(self, stud_id):
        self.students.append(stud_id)

# modify course name
    def modifycourse(self, course_id):
        if course_id == self.c_id:
            print("Course found!")
            self.instr = input("enter new instructor name: ")
            self.c_topic = input("enter new c_topic: ")
            self.c_id = input("enter new course id: ")

# unenrol student
    def unenrol(self, stud_id):
        if stud_id in self.students:
            self.students.remove(stud_id)
        else:
            print("student not found!")

# delete course
    def deletecourse(self, course_id):
        if course_id == self.c_id:
            print("Course found!: ")
            self.instr = ""
            self.c_topic = ""
            self.c_id = ""
            self.students = ""
            self.grades = ""

    def addstudentgrade(self, stud_id):
        for i in range(self.students.__len__()):
            if stud_id in self.students:
                grade = input("enter student grade: ")
                self.grades.insert(i, grade)
                print("grade for ", stud_id, "entered is: ", self.grades[i])
            else:
                print("student not found!")

    def checkgrade(self, stud_id):
        for i in range(self.students.__len__()):
            if stud_id in self.students:
                print("Grade for ", stud_id, "is:", self.grades[i])


class Student():

    def __init__(self):
        self.stud_name = None
        self.stud_id = None
        self.stud_dept = None
        self.studentFlag = False

    def createstudent(self, stud_name, stud_id, stud_dept):
        self.stud_name = stud_name
        self.stud_id = stud_id
        self.stud_dept = stud_dept

    def modifystudent(self, stud_id):
        if stud_id == self.stud_id:
            self.stud_name = input("enter new student name: ")
            self.stud_dept = input("enter new dept: ")
        else:
            print("student not found!")

    def deletestudent(self, stud_id):
        if stud_id == self.stud_id:
            self.stud_name = ""
            self.stud_dept = ""


    def addcourseobject(Course, self=None):
        self.course = Course
        

class Admin:

    def __init__(self, ad_name, ad_pass):
        self.ad_name = ad_name
        self.ad_pass = ad_pass
