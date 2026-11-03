def find_marks(students, name):
    return students[name]


students = {
    "Ayesha": 85,
    "Rahul": 90,
    "Priya": 78,
    "Arjun": 92
}

name = "Priya"

result = find_marks(students, name)

print("Marks --->", result)
