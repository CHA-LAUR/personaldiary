try:
    # Create file if it doesn't exist
    with open("Diary System.txt", "x"):
        print("Diary created")
except FileExistsError:
    print("File already exists")


def add_entry():
    try:
        with open("Diary System.txt", "a") as file:
            while True:
                entry = input("Enter diary entry: ")
                file.write(entry + "\n")

                again = input("Add more? (yes/no): ").lower()
                if again != "yes":
                    break

        print("Entries added.\n")
    except Exception as e:
        print("Error:", e)


def read_entries():
    try:
        with open("Diary System.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("Diary is empty.\n")
            else:
                print("\n--- Your Diary Entries ---")
                print(content)
                print("--------------------------\n")
    except FileNotFoundError:
        print("Diary file not found.\n")


# Menu system
while True:
    print("Personal Diary Application")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")