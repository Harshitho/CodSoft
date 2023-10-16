# Initialize an empty contact list
contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

def view_contact_list():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    search_term = input("Enter a name or phone number to search for a contact: ")
    found_contacts = []
    
    for contact in contacts:
        if (search_term in contact['name']) or (search_term in contact['phone']):
            found_contacts.append(contact)
    
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def update_contact():
    view_contact_list()
    
    if not contacts:
        return
    
    try:
        index = int(input("Enter the number of the contact you want to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("Current Contact Details:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            name = input("Enter the updated name (or press Enter to keep the current name): ")
            phone = input("Enter the updated phone number (or press Enter to keep the current phone number): ")
            email = input("Enter the updated email (or press Enter to keep the current email): ")
            address = input("Enter the updated address (or press Enter to keep the current address): ")
            
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

def delete_contact():
    view_contact_list()
    
    if not contacts:
        return
    
    try:
        index = int(input("Enter the number of the contact you want to delete: ") - 1)
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
