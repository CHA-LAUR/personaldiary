try: 
    with open("Diary System.txt", "x") as filee:
        pass
    print('Diary created')

    with open("Diary System.txt", "w") as filee:
        filee.write("My Diary")

    print("File already exists")

    entry = input("What do you want to write? ")

    with open("Diary System", "a") as filee: 
        
except FileExistsError: ajfkakvja