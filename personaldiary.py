try: 
    with open("Diary System.txt", "x") as file:
        pass
    print('Diary created')

    with open("Diary System.txt", "w") as file:
        file.write("My Diary")

    print("File already exists")

    entry = input("What do you want to write? ")

    with open("Diary System", "a") as file: 
        
except FileExistsError: pangit charys