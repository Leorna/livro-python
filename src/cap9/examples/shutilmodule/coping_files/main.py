import shutil
import os


cwd = os.getcwd()

os.chdir("/home/gabriel")

path = shutil.copy('./teste.txt', cwd+"/algo.txt")

print(path)