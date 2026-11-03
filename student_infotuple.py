def student_info(student):
    name, age, marks = student
    return name, age, marks


student = ("Ayesha", 20, 85)

name, age, marks = student_info(student)

print("Name --->", name)
print("Age --->", age)
print("Marks --->", marks)
