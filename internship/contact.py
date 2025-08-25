contacts = {}

def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact added successfully!")

    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Email: {info['Email']}")
                print(f"Address: {info['Address']}")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"\nName: {search_name}")
            print(f"Phone: {contacts[search_name]['Phone']}")
            print(f"Email: {contacts[search_name]['Email']}")
            print(f"Address: {contacts[search_name]['Address']}")
        else:
            print("Contact not found.")

    elif choice == '4':
        del_name = input("Enter name to delete: ")
        if del_name in contacts:
            del contacts[del_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")