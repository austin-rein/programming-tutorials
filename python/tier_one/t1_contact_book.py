def add_contact(contacts):
    contact = {}
    contact["name"] = input("Enter the contact's name")
    contact["phone"] = input("Enter the contact's phone")
    contact["email"] = input("Enter the contact's email")
    
    contacts.append(contact)
    print("Contact added!")

def view_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

def find_contact(contacts):
    search_contact = input("Enter the contact's name: ")
    for contact in contacts:
        if contact["name"] == search_contact:
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
            return
        else:
            continue
    print("Contact not found")

def save_contacts(contacts):
    with open("contacts.csv", "w") as file:
        for contact in contacts:
            row = f"{contact['name']},{contact['phone']},{contact['email']}\n"
            file.write(row)
    print("Data saved")

def load_contacts():
    contacts = []
    try:
        with open("contacts.csv", "r") as file:
            for line in file:
                contact = {}
                name, phone, email = line.strip().split(",")
                contact['name'] = name
                contact['phone'] = phone
                contact['email'] = email
                contacts.append(contact)
    except FileNotFoundError:
        with open("contacts.csv", "w"):
            print("Initializing new contacts file")
    
    return contacts

def main():
    contacts = load_contacts()
    print("Welcome to the python rolodex")
    while True:
        print(
            "\n1. Add Contact\n" \
            "2. View Contacts\n" \
            "3. Search Contact\n" \
            "4. Exit\n"
        )
        user_choice = input("Enter your choice: ")
        match user_choice:
            case "1":
                add_contact(contacts)
            case "2":
                view_contacts(contacts)
            case "3":
                find_contact(contacts)
            case "4":
                print("Goodbye!")
                save_contacts(contacts)
                break
            case _:
                print("Invalid option")

if __name__ == "__main__":
    main()