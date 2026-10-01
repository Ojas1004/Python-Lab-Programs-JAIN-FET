# attendance = (
#     ("ABC1", "P","A","P"),
#     ("ABC2", "A","P","A"),
#     ("ABC3", "P","P","P"),
#     ("ABC4", "P","P","A")
# )

# print(attendance)

# Student details
students = (
    ("ABC1", "Ojas"),
    ("ABC2", "Omsai"),
    ("ABC3", "Lakshmi"),
    ("ABC4", "Nishtha")
)

# Attendance for two dates
attendance = (
    ("2026-10-01", "ABC1", "P"),
    ("2026-10-01", "ABC2", "A"),
    ("2026-10-01", "ABC3", "P"),
    ("2026-10-01", "ABC4", "P"),

    ("2026-10-02", "ABC1", "P"),
    ("2026-10-02", "ABC2", "A"),
    ("2026-10-02", "ABC3", "A"),
    ("2026-10-02", "ABC4", "A")
)

# attendance percentage
print("Attendance Percentage:")

for student_id, name in students:
    present = 0
    total = 0

    for date, sid, status in attendance:
        if sid == student_id:
            total += 1

            if status == "P":
                present += 1

    percentage = (present / total) * 100

    print(student_id, name, ":", percentage, "%")


# Students with less than 75% attendance
print("\nStudents with less than 75% attendance:")

for student_id, name in students:
    present = 0
    total = 0

    for date, sid, status in attendance:
        if sid == student_id:
            total += 1

            if status == "P":
                present += 1

    percentage = (present / total) * 100

    if percentage < 75:
        print(student_id, name, ":", percentage, "%")