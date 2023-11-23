contacts = {}

def add_contact():
    print("\nAdd Contact")
    name = input("Enter name: ")
    store_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        'store_name': store_name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added.")

def view_contacts():
    print("\nView Contacts")
    if contacts:
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Store Name: {contact_info['store_name']}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("------------------")
    else:
        print("No contacts found.")

def search_contact():
    print("\nSearch Contact")
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"No contact found with the name {name}.")

def update_contact():
    print("\nUpdate Contact")
    name = input("Enter name to update: ")
    if name in contacts:
        new_number = input("Enter new number: ")
        contacts[name] = new_number
        print(f"Contact {name} updated with new number {new_number}.")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact():
    print("\nDelete Contact")
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"No contact found with the name {name}.")

if __name__ == "__main__":
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
