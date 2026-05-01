try: 
    with open("Diary System.txt", "x") as file:
        pass
    print('Diary created')

    with open("Diary System.txt", "w") as file:
        file.write(input("What do you want to write??"))
        def add_entry():
    try:
        with open("diary.txt", "a") as file:
            while True:
                entry = input("Enter diary entry: ")
                file.write(entry + "\n")

                again = input("Add more? (yes/no): ").lower()
                if again != "yes":
                    break

        print("Entries added.")
    except Exception as e:
        print("Error:", e)

add_entry()
Compose
Write to Charys Betasolo Mondelo

        
except FileExistsError:
    print ("File already exists")
    
