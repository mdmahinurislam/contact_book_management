# File: contact_book.py

# Import necessary modules
import os

# Constants
FILE_NAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split("|")
                contacts.append({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address
                })
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['email']}|{contact['phone']}|{contact['address']}\n")

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()

    # Check for duplicate phone number or email
    for contact in contacts:
        if contact['phone'] == phone:
            print("Error: A contact with this phone number already exists.")
            return
        if contact['email'] == email:
            print("Error: A contact with this email already exists.")
            return

    contacts.append({"name": name, "email": email, "phone": phone, "address": address})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

# Remove a contact
def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ").strip()
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact removed successfully!")
            return

    print("Error: Contact not found.")

# Search for a contact
def search_contact(contacts):
    query = input("Enter name, email, or phone to search: ").strip()
    results = [contact for contact in contacts if query in contact['name'] or query in contact['email'] or query in contact['phone']]

    if not results:
        print("No contacts found.")
        return

    print("\nSearch Results:")
    for index, contact in enumerate(results, start=1):
        print(f"{index}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
