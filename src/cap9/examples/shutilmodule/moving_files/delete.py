import os


os.chdir('/home/gabriel')

try:
    os.unlink('./teste.txt')
except:
    print("File does not exist")
else:
    print("File deleted")