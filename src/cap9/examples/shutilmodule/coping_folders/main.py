import os
import shutil


cwd = os.getcwd()

os.chdir('/home/gabriel')

try:
    new_path = shutil.copytree('./Imagens', cwd+"/novas_imagens")
except:
    print('Folder already copied')
else:
    print(new_path)