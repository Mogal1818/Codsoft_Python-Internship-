import json

class ContactBook:
    def __init__(self):
        self.contacts = []

    def load_contacts(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        self.save_contacts()

    def view_contacts(self):
        print("Contact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact['name'] or search_term in contact['phone']]
        if results:
            for contact in results:
                self.print_contact(contact)
        else:
            print("No contacts found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.print_contact(contact)
                contact['name'] = input("Enter new name: ") or contact['name']
                contact['phone'] = input("Enter new phone: ") or contact['phone']
                contact['email'] = input("Enter new email: ") or contact['email']
                contact['address'] = input("Enter new address: ") or contact['address']
                self.save_contacts()
                print("Contact updated.")
                return
        print("No contact found to update.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted.")
                return
        print("No contact found to delete.")

    def print_contact(self, contact):
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print("-" * 20)

def main():
    contact_book = ContactBook()
    contact_book.load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone to update: ")
            contact_book.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
