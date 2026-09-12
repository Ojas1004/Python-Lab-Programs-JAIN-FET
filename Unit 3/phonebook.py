# stud = []
# name = input("Enter student name: ")
# age = int(input("Enter student age: "))
# phone_number = int(input("Enter Student Phone Number:"))
# student_city = input("Enter Student's City:")
# student = {
#     "name": name,
#     "age": age,
#     "phone number": phone_number,
#     "student city": student_city
# }
# stud.append(student)
# print(stud)


# stud = []

# n = int(input("How many students? "))
# for i in range(n):
#     name = input("Enter student name: ")
#     age = int(input("Enter student age: "))
#     city = input("Enter student city: ")
#     phone = input("Enter student phone number: ")

#     student = {
#         "name": name,
#         "age": age,
#         "city": city,
#         "phone": phone
#     }

#     stud.append(student)

# print("\nAll Students:")
# print(stud)



# name = input("\nEnter student name to update: ")

# for student in stud:
#     if student["name"] == name:
#         student["age"] = int(input("Enter new age: "))
#         student["city"] = input("Enter new city: ")
#         student["phone"] = input("Enter new phone number: ")

#         print("Data updated successfully!")
#         break
# else:
#     print("Student not found!")


# name = input("\nEnter student name to delete: ")

# for student in stud:
#     if student["name"] == name:
#         stud.remove(student)
#         print("Data deleted successfully!")
#         break
# else:
#     print("Student not found!")


# print("\nFinal Data:")
# print(stud)


contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully.")

    # View contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- ALL CONTACTS ---")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("-------------------")

    # Search contact
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)

                print("Contact deleted successfully.")

                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice.")

