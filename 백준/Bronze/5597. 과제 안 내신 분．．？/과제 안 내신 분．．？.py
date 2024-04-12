submitted_students = set()
for _ in range(28):
    submitted_students.add(int(input()))

for student in range(1, 31):
    if student not in submitted_students:
        print(student)
        break

for student in range(student + 1, 31):
    if student not in submitted_students:
        print(student)
        break
