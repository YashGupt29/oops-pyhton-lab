import math as m
class Student_Data:
    name = ""
    marks = []
    grades = []
    sub = 0
    grade_points = []

    def __init__(self,name,marks,subjects):
        self.name = name
        self.marks  = marks
        self.sub=subjects


    def change_marks(self):
        for i in range(0,sub):
            temp = int(input(f"Enter updated marks in subject {i+1} : "))
            self.marks[i]=temp
        print("Marks successfully updated!")
        

    def average_marks(self):
        summ = sum(marks)
        average = float(summ/sub)
        return average


    def grade_calculation(self):
        for i in self.marks:
            self.grade_points.append(m.ceil(i//10))
            if i>=90:
                self.grades.append('EX')
            elif i>=80:
                self.grades.append('A')
            elif i>=70:
                self.grades.append('B')
            elif i>=60:
                self.grades.append('C')
            elif i>=50:
                self.grades.append('D')
            elif i>40:
                self.grades.append('P')
            else:
                self.grades.append('F')

    

    def SGPA(self):
        summ = sum(self.grade_points)
        sgpa = float(summ/sub)
        return sgpa


    def print(self):
        print("\nName : ",self.name)
        print("Average marks : ",self.average_marks())
        print("\nGrades Obtained")
        for i in range(0,sub):
            print(f"Subject {i+1} : {self.grades[i]}")
        print("\nSGPA obtained : ", self.SGPA())


name = input("Enter name of the student : ")
sub = int(input("Enter number of subjects : "))
marks=[]
for i in range (0,sub):
    temp = int(input(f"Enter marks of subject {i+1} : "))
    marks.append(temp)

student = Student_Data(name, marks, sub)

print("Do you wish to change the marks in any subject?")
choice = input("Enter Y(or y) for yes and N(or n) for no : ")
if choice== 'Y' or choice == 'y':
    student.change_marks()

print("\n--------------------------")
student.grade_calculation()
student.print()
