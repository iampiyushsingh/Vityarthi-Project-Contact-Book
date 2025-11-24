import os

CONTACTS_FILE = "contacts.txt"


# -------------------- Helper Functions --------------------

def load_contacts():
    """Load all contacts from the file into a list of dictionaries."""
    contacts = []
    if not os.path.exists(CONTACTS_FILE):
        return contacts
    
    with open(CONTACTS_FILE, "r") as f:
        for line in f:
            name, phone, email = line.strip().split("|")
            contacts.append({"name": name, "phone": phone, "email": email})
    return contacts


def save_contacts(contacts):
    """Save the list of contacts back to the file."""
    with open(CONTACTS_FILE, "w") as f:
        for c in contacts:
            f.write(f"{c['name']}|{c['phone']}|{c['email']}\n")


# -------------------- Features --------------------

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

    print("\nContact added successfully!\n")


def search_contact():
    query = input("Search by name or phone: ").lower()
    contacts = load_contacts()

    found = False
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            print("\n--- Contact Found ---")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}\n")
            found = True

    if not found:
        print("\nNo matching contact found.\n")


def list_contacts():
    contacts = load_contacts()

    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n--- All Contacts ---")
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")
    print()


def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    contacts = load_contacts()

    for c in contacts:
        if c["name"].lower() == name:
            print("\nLeave field blank to keep old value.\n")

            new_name = input(f"New name ({c['name']}): ") or c["name"]
            new_phone = input(f"New phone ({c['phone']}): ") or c["phone"]
            new_email = input(f"New email ({c['email']}): ") or c["email"]

            c["name"] = new_name
            c["phone"] = new_phone
            c["email"] = new_email

            save_contacts(contacts)
            print("\nContact updated successfully!\n")
            return

    print("\nContact not found.\n")


def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load_contacts()

    new_contacts = [c for c in contacts if c["name"].lower() != name]

    if len(new_contacts) == len(contacts):
        print("\nContact not found.\n")
        return

    save_contacts(new_contacts)
    print("\nContact deleted successfully!\n")


# -------------------- Main Menu --------------------

def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            list_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
