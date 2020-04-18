import os


cwd = os.getcwd()##returns the current work directory
print("-> Old cwd: " + cwd)


os.chdir("/home/gabriel") ##changing the cwd

print("-> New cwd: " + os.getcwd())

try:
    ## makes directories, creates the GABRIEL folder and inside of it creates the IMAGES folder
    os.makedirs("./GABRIEL/IMAGES") 
except FileExistsError:
    print("File exists")