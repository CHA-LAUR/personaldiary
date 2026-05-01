try: 
    with open("Diary System.txt", "x") as file:
        pass
    print('Diary created')

    with open("Diary System.txt", "w") as file:
        file.write(input("What do you want to write?"))
        
except FileExistsError:
    print ("File already exists")