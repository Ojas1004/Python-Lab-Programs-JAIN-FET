
import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Basic", "Allowance",
                         "Deduction", "Net Salary"])

        for i in range(n):
            print("\nEnter Employee Details")

            emp_id = input("Employee ID: ")
            name = input("Employee Name: ")

            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([emp_id, name, basic, allowance,
                             deduction, net_salary])

    print("\nPayroll records saved successfully")

    print("\nEmployee Payroll Records:")

    with open("payroll.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except ValueError:
    print("Invalid input, please enter numeric values.")

except Exception as e:
    print("Error:", e)
