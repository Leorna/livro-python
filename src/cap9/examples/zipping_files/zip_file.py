import zipfile
import os


os.chdir('/home/gabriel')

zfile = zipfile.ZipFile('cats.zip')

print(zfile.namelist())


cats_txt = zfile.getinfo('cats/catnames.txt')

print(f'cats.txt size: {cats_txt.file_size}')
print(f'cats.txt compressed size: {cats_txt.compress_size}')


print('Compressed file is {}x smaller!'.format(round(cats_txt.file_size / cats_txt.compress_size)))


zfile.close()