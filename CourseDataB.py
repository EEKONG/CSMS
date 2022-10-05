class StudentDataB:

    def __init__(self):
        self.students_list = list()

    def addstudenttodb(self, stud_id):
        self.students_list.append(stud_id)

    def modifyCourse(self, course_id):
        for i in range(self.c_list.__len__()):
            if course_id in self.c_list:
                print("Course found!")
                course_id = input("enter new c_id: ")
                self.c_list[i] = course_id
                self.c_id = course_id

    def deleteStudent(self, stud_id):
        for i in range(self.students_list.__len__()):
            if stud_id in self.students_list:
                self.students_list.remove(stud_id)
            else:
                print("student not found!")
