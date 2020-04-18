import shelve


shelf_file = shelve.open("../shelf_binaries/mydata")

print(shelf_file["people"])

shelf_file.close()