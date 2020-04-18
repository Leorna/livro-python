file = open("../simple_files/market_list.txt", "a+")


while True:
    item = input("Enter an item to the market list: ")

    file.write("\n-{}".format(item))

    op = input("Do you want to insert more items? [s|n] ").lower()

    if op == 'n':
        break
    elif op != 's':
        while op != 'n' and op != 's':
            op = input("Do you want to insert more items? [s|n] ").lower()
        if op == 'n':
            break


file.seek(0)

print("Your list:{}".format(file.read()))

file.close()
