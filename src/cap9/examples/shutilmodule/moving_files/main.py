import os
import shutil


cwd = os.getcwd()

os.chdir('/home/gabriel')


try:
    new_path = shutil.move('./teste', cwd)
except:
    print("Folder or file does not exist")
else:
    print(new_path)