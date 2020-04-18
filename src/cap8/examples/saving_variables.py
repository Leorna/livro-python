import shelve


shelf_file = shelve.open("../shelf_binaries/mydata")


try:
    people = shelf_file["people"]
except:
    people = []
    

while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    people.append({name: age})

    op = input("Do you want to insert more items? [y|n] ").lower()

    if op == 'n':
        break
    elif op != 'y':
        while op != 'n' and op != 'y':
            op = input("Do you want to insert more items? [y|n] ").lower()
        if op == 'n':
            break


shelf_file["people"] = people

shelf_file.close()