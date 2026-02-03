import json

def save_password():
    website = input("Website: ")
    email = input("Email: ")
    password = input("Password: ")

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        print("Saved successfully.")

def find_password():
    website = input("Website to search: ")

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(f"Email: {data[website]['email']}")
            print(f"Password: {data[website]['password']}")
    except FileNotFoundError:
        print("No data file found.")
    except KeyError:
        print("Website not found.")

while True:
    choice = input("Type 'save', 'find', or 'exit': ").lower()
    if choice == "save":
        save_password()
    elif choice == "find":
        find_password()
    elif choice == "exit":
        break
