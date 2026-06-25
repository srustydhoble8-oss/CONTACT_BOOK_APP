contacts = {}

def add_contact():
    contacts[name] = mobile
    return "successful"

def view_contact():
    return contacts

def search_contact():
    if name in contacts:
        return contacts[name]
        
    else:
        print("❌ Contact Not Found!")

def delete_contact():
    if name in  contacts:
        del contacts[name]
        return "successful"
    else:
        print("❌ Contact Not Found!")



while True:
    print("\n📱 ===== CONTACT BOOK ===== 📱")
    print("1️⃣  Add Contact")
    print("2️⃣  View Contacts")
    print("3️⃣  Search Contact")
    print("4️⃣  Delete Contact")
    print("5️⃣  Exit")
    print("=" * 30)
    
    choice = input("Enter your choice(1-5): ")

    if not choice.isdigit():
        print("❌ Please enter numbers only!")
        continue

    choice = int(choice)

    if choice == 5:
        print("👋Bye, Thanks for using Contact Book!")
        break

    if choice == 1:

        name = input("Enter name: ")
        mobile = input("Enter mobile in 10 digit: ")

        print(f"add contact {add_contact()}")
        print("✅ Contact Added Successfully!")

    elif choice == 2:
        print(f"view contact {view_contact()}")

    elif choice == 3:
        name = input("Enter name: ")
        print("🔍 Contact Found:", search_contact())

    elif choice == 4:
        name = input("Enter name: ")
        print(f"🗑️ Contact Deleted Successfully! {delete_contact()}")
    
    else:
        print("Invalid option.Please choice your option between(1-5)")

