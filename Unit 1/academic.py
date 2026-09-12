name = input("enter your name: ")
usn = input("enter USN: ")
branch = input("Enter Branch: ")
semester = int(input("Enter Semester: "))

mark1 = float(input("enter marks in subject 1:"))
mark2 = float(input("enter marks in subject 2:"))
mark3 = float(input("enter marks in subject 3:"))

total = mark1 + mark2 + mark3
average = total/3

print("\n STUDENT REPORT")
print(f"Name : {name}")
print(f"USN : {usn}")
print(f"Branch : {branch}")
print(f"Semester : {semester}")
print(f"total marks: {total}")
print(f"Average : {average:.2f}")

