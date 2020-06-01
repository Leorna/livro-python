import os
import zipfile


os.chdir('/home/gabriel')


zfile = zipfile.ZipFile('cats.zip')


os.chdir('/home/gabriel/Documentos')

zfile.extractall()

zfile.close()