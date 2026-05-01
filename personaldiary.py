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

        print("Entries added.")
    except Exception as e:
        print("Error:", e)

# Run the function
add_entry()