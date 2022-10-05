class StudentDataB:

    def __init__(self):
        self.student_list = list()

    def addstudenttodb(self, stud_id):
        self.student_list.append(stud_id)

    def deleteStudent(self, stud_id):
        for i in range(self.student_list.__len__()):
            if stud_id in self_student_list:
                self.student_list.remove(stud_id)
            else:
                print("student not found!")
