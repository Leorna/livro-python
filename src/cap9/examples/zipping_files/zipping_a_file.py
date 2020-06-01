import os
import zipfile
import shutil


cwd = os.getcwd()

os.chdir('/home/gabriel')


new_zip = zipfile.ZipFile('delicious.zip', 'w')


new_zip.write('delicious', compress_type=zipfile.ZIP_DEFLATED)

new_zip.close()


try:
    shutil.move('delicious.zip', cwd)
except:
    print('File does not exist')
else:
    print('File moved')