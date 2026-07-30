class Student:
    def __init__(self,department,degree,gpa):
        self.department=department
        self.degree=degree
        self.gpa=gpa

s1=Student('computer','Bachelor',3.0)
s2=Student('finance','Master',3.5)
s3=Student("law",'Doctor',3.6)

print(s1.degree)
print(s2.department)
print(s3.gpa)


